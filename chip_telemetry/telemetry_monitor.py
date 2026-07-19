import json
import random
from datetime import datetime


class ThermalMonitor:

    def collect(self):
        return {
            "cpu_temperature_c": round(random.uniform(40,55),2),
            "gpu_temperature_c": round(random.uniform(50,70),2),
            "ai_accelerator_temperature_c": round(random.uniform(55,75),2),
            "cooling_status": "ACTIVE"
        }


class ComputeMonitor:

    def collect(self):
        return {
            "cpu_usage_percent": random.randint(30,80),
            "gpu_usage_percent": random.randint(40,90),
            "inference_latency_ms": random.randint(20,120),
            "requests_per_second": random.randint(500,2000)
        }


class MemoryMonitor:

    def collect(self):
        return {
            "ram_usage_percent": random.randint(40,75),
            "agent_memory_records": random.randint(8000,20000),
            "knowledge_graph_nodes": random.randint(100000,300000),
            "cache_hit_rate_percent": random.randint(85,99)
        }


class AIHealthScore:

    def calculate(self, thermal, compute, memory):

        score = 100

        if thermal["ai_accelerator_temperature_c"] > 80:
            score -= 10

        if compute["inference_latency_ms"] > 100:
            score -= 10

        if memory["cache_hit_rate_percent"] < 90:
            score -= 5

        return {
            "overall_score": score,
            "status":
                "OPTIMAL"
                if score >= 90
                else "WARNING"
        }


class AEONChipTelemetry:

    def generate(self):

        thermal = ThermalMonitor().collect()
        compute = ComputeMonitor().collect()
        memory = MemoryMonitor().collect()

        health = AIHealthScore().calculate(
            thermal,
            compute,
            memory
        )

        return {
            "system":
                "AEON MATRIX CHIP INTELLIGENCE",

            "timestamp":
                datetime.utcnow().isoformat(),

            "thermal":
                thermal,

            "compute":
                compute,

            "memory":
                memory,

            "ai_health":
                health
        }


if __name__ == "__main__":

    monitor = AEONChipTelemetry()

    result = monitor.generate()

    print("="*65)
    print(" AEON MATRIX CHIP TELEMETRY MONITOR ")
    print("="*65)

    print(json.dumps(
        result,
        indent=2
    ))
