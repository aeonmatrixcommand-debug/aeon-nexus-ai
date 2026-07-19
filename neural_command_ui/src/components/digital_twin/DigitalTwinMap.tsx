import React, {useState} from "react";


interface TwinNode {

    id:string;
    name:string;
    type:string;
    temperature:number;
    workload:number;
    status:string;

}


const initialNodes:TwinNode[] = [

{
id:"cpu",
name:"CPU Intelligence Cluster",
type:"COMPUTE",
temperature:58,
workload:62,
status:"OPTIMAL"
},

{
id:"gpu",
name:"GPU Neural Engine",
type:"AI_ACCELERATION",
temperature:67,
workload:74,
status:"OPTIMAL"
},

{
id:"memory",
name:"Memory Fabric",
type:"STORAGE",
temperature:72,
workload:81,
status:"WARNING"
},

{
id:"agents",
name:"Multi Agent Network",
type:"AI_AGENT",
temperature:55,
workload:45,
status:"OPTIMAL"
}

];



export default function DigitalTwinMap(){


const [nodes,setNodes] =
useState(initialNodes);


const [selected,setSelected] =
useState<TwinNode|null>(null);



function simulateFailure(){

setNodes(nodes.map(node=>{

if(node.id==="gpu"){

return {

...node,

temperature:92,

workload:98,

status:"CRITICAL"

};

}

return node;

}));

}



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
🌐 AEON MATRIX DIGITAL TWIN MAP
</h1>


<button
onClick={simulateFailure}
>
⚠ Simulate AI Node Failure
</button>



{

nodes.map(node=>(


<div
key={node.id}

onClick={()=>setSelected(node)}

style={{

margin:"15px",

padding:"18px",

border:
"1px solid #00ffd5",

borderRadius:"15px",

cursor:"pointer"

}}

>


<h2>
{node.name}
</h2>


<p>
Type:
{node.type}
</p>


<p>
Temperature:
{node.temperature}°C
</p>


<p>
Workload:
{node.workload}%
</p>


<p>
State:
{node.status}
</p>


</div>


))

}



{

selected && (

<div>

<h2>
🔎 NODE INSPECTOR
</h2>


<p>
{selected.name}
</p>

<p>
Status:
{selected.status}
</p>


<p>
Risk:
{
selected.status==="CRITICAL"
?
"HIGH"
:
"LOW"
}
</p>


</div>

)

}


</div>

)

}
