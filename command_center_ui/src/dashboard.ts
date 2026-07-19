export interface AEONStatus {
  system: string;
  status: string;
  risk_score?: number;
  decision?: string;
}

export async function getHealth() {
  const res = await fetch("http://127.0.0.1:8090/health");
  return await res.json();
}

export async function getDecision(event:string) {
  const res = await fetch(
    "http://127.0.0.1:8090/decision",
    {
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        event,
        system:"WMS",
        impact:"Operational Analysis"
      })
    }
  );

  return await res.json();
}

console.log("AEON MATRIX COMMAND CENTER ONLINE");
