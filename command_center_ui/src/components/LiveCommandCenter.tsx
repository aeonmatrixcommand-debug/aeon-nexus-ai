import {useEffect, useState} from "react";
import {getHealth, getDecision} from "../dashboard";

export default function LiveCommandCenter(){

  const [health,setHealth] = useState<any>(null);
  const [decision,setDecision] = useState<any>(null);

  useEffect(()=>{
    getHealth().then(setHealth);

    getDecision(
      "Warehouse inventory mismatch detected"
    ).then(setDecision);

  },[]);

  return (
    <main>
      <h1>AEON MATRIX LIVE COMMAND CENTER</h1>

      <h2>System</h2>
      <pre>
        {JSON.stringify(health,null,2)}
      </pre>

      <h2>Decision Intelligence</h2>
      <pre>
        {JSON.stringify(decision,null,2)}
      </pre>

    </main>
  );
}
