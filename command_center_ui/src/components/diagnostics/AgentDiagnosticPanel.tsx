import React,{useEffect,useState} from "react";


interface Agent {

 id:string;

 role:string;

 load:number;

 latency:number;

 health:number;

 status:string;

}



export default function AgentDiagnosticPanel(){


const [open,setOpen]=useState(true);


const [agents,setAgents]=useState<Agent[]>([

{
id:"AG-001",
role:"Guardian AI",
load:42,
latency:120,
health:98,
status:"OPTIMAL"
},

{
id:"AG-002",
role:"Forecast AI",
load:78,
latency:240,
health:82,
status:"WARNING"
},

{
id:"AG-003",
role:"Recovery AI",
load:91,
latency:410,
health:64,
status:"HOT THREAD"
},

{
id:"AG-004",
role:"Optimization AI",
load:55,
latency:160,
health:94,
status:"OPTIMAL"
}

]);



useEffect(()=>{


const timer=setInterval(()=>{


setAgents(old=>

old.map(a=>({

...a,

load:
Math.min(
100,
Math.max(
10,
a.load+
Math.floor(Math.random()*9)-4
)
),

latency:
Math.max(
50,
a.latency+
Math.floor(Math.random()*30)-15
)

}))


)


},1500);


return()=>clearInterval(timer);


},[]);




return (

<div
style={{
background:"#020617",
color:"#e2e8f0",
padding:"20px",
borderRadius:"18px"
}}
>


<button
onClick={()=>setOpen(!open)}
>

{open?"▼":"▶"}

 AGENT DIAGNOSTIC PANEL

</button>



{open &&

agents.map(agent=>(


<div
key={agent.id}
style={{
marginTop:"15px",
padding:"15px",
border:"1px solid #334155",
borderRadius:"12px"
}}
>


<h3>

{agent.id}

</h3>


<p>

Role:

{agent.role}

</p>


<p>

Load:

{agent.load}%

</p>


<p>

Latency:

{agent.latency} ms

</p>


<p>

Health:

{agent.health}/100

</p>


<strong>

Status:

{agent.status}

</strong>


</div>


))


}


</div>

)


}
