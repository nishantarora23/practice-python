from pathlib import Path
import re

pattern = re.compile(r"^server=(?P<server>[a-z0-9]+)\s+" \
          r"cpu=(?P<cpu>\d+)\%\s+" \
          r"memory=(?P<memory>\d+)\%\s*$")

metrics = {}
malformed_line = 0

server_file = Path("./server_metrics.txt")
if server_file.is_file():
    with open(server_file, "r") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                server_name = match.group("server")
                try:
                    cpu = int(match.group("cpu"))
                    memory = int(match.group("memory"))
                except ValueError as e:
                    print(f"Invalid type conversion")
                metrics.setdefault(server_name, {
                        "cpu": [],
                        "memory": []
                    })
                metrics[server_name]["cpu"].append(cpu)
                metrics[server_name]["memory"].append(memory)
            else:
                malformed_line = malformed_line + 1

print("Server metrics summary:")
for k, v in metrics.items():
    cpu_usage = sum(v["cpu"])/len(v["cpu"])
    memory_usage = sum(v["memory"]) / len(v["memory"])
    print(f"{k} -> CPU: {cpu_usage:.1f}%, Memory: {memory_usage:.1f}%")

if malformed_line > 0:
    print(f"Malformed lines: {malformed_line}")



