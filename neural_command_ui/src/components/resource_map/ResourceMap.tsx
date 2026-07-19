import React from "react";


interface Node {

    name:string;
    usage:number;
    status:string;

}


const nodes:Node[] = [

    {
        name:"CPU Cluster",
        usage:62,
        status:"OPTIMAL"
    },

    {
        name:"GPU Compute",
        usage:74,
        status:"OPTIMAL"
    },

    {
        name:"AI Accelerator",
        usage:58,
        status:"OPTIMAL"
    },

    {
        name:"Memory Fabric",
        usage:81,
        status:"WARNING"
    },

    {
        name:"Agent Network",
        usage:45,
        status:"OPTIMAL"
    }

];



export default function ResourceMap(){


return (

<div
style={{
background:"#030712",
color:"#00ffcc",
padding:"24px",
borderRadius:"20px",
fontFamily:"monospace"
}}
>

<h1>
🗺 AEON MATRIX RESOURCE MAP
</h1>


{

nodes.map((node,index)=>(


<div
key={index}
style={{

margin:"15px",
padding:"15px",
border:
"1px solid #00ffcc",

borderRadius:"12px"

}}
>


<h2>
{node.name}
</h2>


<p>
Workload:
{node.usage}%
</p>


<p>
Status:
{node.status}
</p>


<div>

{"█".repeat(
Math.floor(node.usage/10)
)}

</div>


</div>


))


}


</div>

)

}
