import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  apiKey: import.meta.env.VITE_GEMINI_API_KEY
});

const button = document.getElementById("run");
const input = document.getElementById("prompt") as HTMLInputElement;
const output = document.getElementById("output");

button?.addEventListener("click", async () => {

  if (!output) return;

  output.textContent = "Gemini Processing...";

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-lite",
    contents: input.value
  });

  output.textContent =
    response.text || "No response";

});
