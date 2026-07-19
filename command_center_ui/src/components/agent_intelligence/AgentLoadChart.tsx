import React,{useEffect,useState} from "react";


interface AgentLoad {

    name:string;
    load:number;
    status:string;

}


export default function AgentLoadChart(){


const [agents,setAgents] =
useState<AgentLoad[]>([

{
name:"Guardian AI",
load:42,
status:"OPTIMAL"
},

{
name:"Forecast AI",
load:78,
status:"WARNING"
},

{
name:"Recovery AI",
load:91,
status:"BOTTLENECK"
},

{
name:"Optimization AI",
load:55,
status:"OPTIMAL"
}

]);



useEffect(()=>{


const timer=setInterval(()=>{


setAgents(old=>

old.map(agent=>({

...agent,

load:
Math.min(
100,
Math.max(
20,
agent.load + Math.floor(Math.random()*11)-5
)

)

}))


)


},2000);



return()=>clearInterval(timer);


},[]);





return (

<div
style={{
background:"#020617",
color:"#00ffd5",
padding:"25px",
borderRadius:"20px"
}}
>


<h1>
🤖 AI AGENT LOAD DISTRIBUTION
</h1>


{

agents.map(agent=>(


<div
key={agent.name}
style={{
marginBottom:"20px"
}}
>


<div>

{agent.name}

&nbsp;

{agent.load}%

</div>



<div
style={{

height:"20px",

background:"#111827",

borderRadius:"10px"

}}
>


<div

style={{

width:`${agent.load}%`,

height:"100%",

background:
agent.load>85
?
"#ef4444"
:
agent.load>70
?
"#eab308"
:
"#22c55e",

borderRadius:"10px"

}}

>


</div>

</div>



<p>

Status:

{agent.status}

</p>


</div>


))

}


<h2>

⚠ Bottleneck Analysis

</h2>


<p>

{

agents.find(
a=>a.load>85
)?.name

||

"No bottleneck detected"

}

</p>


</div>

)

}
