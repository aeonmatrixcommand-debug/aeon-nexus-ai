const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");

const statusBox = document.getElementById("status");
const transcriptBox = document.getElementById("transcript");
const responseBox = document.getElementById("response");

let socket = null;
let audioContext = null;
let mediaStream = null;
let sourceNode = null;
let processorNode = null;
let muteNode = null;

let playbackTime = 0;
let stopRequested = false;

let userTranscript = "";
let modelTranscript = "";


function setStatus(text) {
  statusBox.textContent = text;
}


function downsampleTo16k(input, inputRate) {
  const targetRate = 16000;

  if (inputRate === targetRate) {
    return floatToInt16(input);
  }

  const ratio = inputRate / targetRate;
  const outputLength = Math.round(input.length / ratio);
  const output = new Int16Array(outputLength);

  let inputOffset = 0;

  for (let i = 0; i < outputLength; i++) {
    const nextOffset = Math.round((i + 1) * ratio);

    let sum = 0;
    let count = 0;

    for (
      let j = inputOffset;
      j < nextOffset && j < input.length;
      j++
    ) {
      sum += input[j];
      count++;
    }

    const sample = count ? sum / count : 0;
    const clipped = Math.max(-1, Math.min(1, sample));

    output[i] = clipped < 0
      ? clipped * 32768
      : clipped * 32767;

    inputOffset = nextOffset;
  }

  return output;
}


function floatToInt16(input) {
  const output = new Int16Array(input.length);

  for (let i = 0; i < input.length; i++) {
    const sample = Math.max(-1, Math.min(1, input[i]));

    output[i] = sample < 0
      ? sample * 32768
      : sample * 32767;
  }

  return output;
}


function playPCM24k(arrayBuffer) {
  const view = new DataView(arrayBuffer);
  const samples = view.byteLength / 2;

  const floats = new Float32Array(samples);

  for (let i = 0; i < samples; i++) {
    floats[i] =
      view.getInt16(i * 2, true) / 32768;
  }

  const buffer = audioContext.createBuffer(
    1,
    samples,
    24000
  );

  buffer.copyToChannel(floats, 0);

  const source = audioContext.createBufferSource();
  source.buffer = buffer;
  source.connect(audioContext.destination);

  const startAt = Math.max(
    audioContext.currentTime,
    playbackTime
  );

  source.start(startAt);

  playbackTime =
    startAt + buffer.duration;
}


async function startVoice() {
  stopRequested = false;
  userTranscript = "";
  modelTranscript = "";

  transcriptBox.textContent = "กำลังฟัง...";
  responseBox.textContent = "—";

  const wsProtocol =
    location.protocol === "https:"
      ? "wss"
      : "ws";

  socket = new WebSocket(
    `${wsProtocol}://${location.host}/ws/voice/th`
  );

  socket.binaryType = "arraybuffer";

  socket.onopen = async () => {
    try {
      setStatus("กำลังขอสิทธิ์ใช้ไมโครโฟน...");

      audioContext = new AudioContext();

      await audioContext.resume();

      playbackTime = audioContext.currentTime;

      mediaStream =
        await navigator.mediaDevices.getUserMedia({
          audio: {
            channelCount: 1,
            echoCancellation: true,
            noiseSuppression: true,
            autoGainControl: true,
          },
          video: false,
        });

      sourceNode =
        audioContext.createMediaStreamSource(
          mediaStream
        );

      processorNode =
        audioContext.createScriptProcessor(
          4096,
          1,
          1
        );

      muteNode = audioContext.createGain();
      muteNode.gain.value = 0;

      sourceNode.connect(processorNode);
      processorNode.connect(muteNode);
      muteNode.connect(audioContext.destination);

      processorNode.onaudioprocess = event => {
        if (
          !socket ||
          socket.readyState !== WebSocket.OPEN
        ) {
          return;
        }

        const input =
          event.inputBuffer.getChannelData(0);

        const pcm =
          downsampleTo16k(
            input,
            audioContext.sampleRate
          );

        socket.send(pcm.buffer);
      };

      startButton.disabled = true;
      stopButton.disabled = false;

      setStatus(
        "กำลังฟังภาษาไทย — พูดได้เลย"
      );

    } catch (error) {
      setStatus(
        "ไม่สามารถเปิดไมโครโฟน: " +
        error.message
      );
    }
  };


  socket.onmessage = async event => {
    if (event.data instanceof ArrayBuffer) {
      playPCM24k(event.data);
      return;
    }

    const message = JSON.parse(event.data);

    if (message.type === "status") {
      setStatus(
        "Gemini Live เชื่อมต่อแล้ว"
      );
    }

    if (message.type === "input_transcript") {
      userTranscript += message.text;

      transcriptBox.textContent =
        userTranscript;
    }

    if (message.type === "output_transcript") {
      modelTranscript += message.text;

      responseBox.textContent =
        modelTranscript;
    }

    if (message.type === "interrupted") {
      playbackTime =
        audioContext.currentTime;

      setStatus(
        "ตรวจพบการพูดแทรก"
      );
    }

    if (message.type === "turn_complete") {
      setStatus(
        "ตอบกลับเสร็จแล้ว"
      );

      if (stopRequested && socket) {
        socket.close();
      }
    }
  };


  socket.onerror = () => {
    setStatus(
      "เกิดข้อผิดพลาดในการเชื่อมต่อ Voice Gateway"
    );
  };


  socket.onclose = () => {
    startButton.disabled = false;
    stopButton.disabled = true;
  };
}


function stopVoice() {
  stopRequested = true;

  if (processorNode) {
    processorNode.disconnect();
    processorNode = null;
  }

  if (sourceNode) {
    sourceNode.disconnect();
    sourceNode = null;
  }

  if (mediaStream) {
    mediaStream
      .getTracks()
      .forEach(track => track.stop());

    mediaStream = null;
  }

  if (
    socket &&
    socket.readyState === WebSocket.OPEN
  ) {
    socket.send(
      JSON.stringify({
        type: "audio_end"
      })
    );
  }

  stopButton.disabled = true;

  setStatus(
    "หยุดฟังแล้ว — กำลังประมวลผลคำตอบ"
  );
}


startButton.addEventListener(
  "click",
  startVoice
);

stopButton.addEventListener(
  "click",
  stopVoice
);
