import React, {useState} from "react";


export default function CommandControlPanel(){

const [mode,setMode] = useState("LIVE");


function snapshot(){

    const data = {

        system:
        "AEON MATRIX NEURAL CORE",

        time:
        new Date().toISOString(),

        mode,

        status:
        "CAPTURED"

    };


    localStorage.setItem(
        "aeon_snapshot",
        JSON.stringify(data)
    );


    alert(
        "System Snapshot Saved"
    );
}



function fullscreen(){

    document.documentElement.requestFullscreen?.();

}



return (

<div
style={{
background:"#050914",
padding:"20px",
borderRadius:"16px",
color:"#00ffd5"
}}
>

<h2>
🧠 COMMAND CENTER CONTROLS
</h2>


<button onClick={snapshot}>
📸 System Snapshots
</button>


<button onClick={fullscreen}>
⛶ Full-Screen Toggle
</button>


<button
onClick={()=>setMode("RESOURCE_MAP")}
>
🗺 Resource Map
</button>


<button
onClick={()=>setMode("DIAGNOSTICS")}
>
🔍 Live Diagnostics
</button>


<button
onClick={()=>setMode("AGENT_NETWORK")}
>
🤖 Agent Network
</button>


<div>

<h3>
CURRENT MODE
</h3>

<p>
{mode}
</p>

</div>


</div>

);

}
