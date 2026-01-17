# Problem: Server Metrics Aggregator

## Scenario

You have a log file called server_metrics.txt with lines representing CPU and memory usage:
```
server=web01 cpu=20% memory=35%
server=db01 cpu=55% memory=70%
server=web01 cpu=25% memory=40%
server=db01 cpu=bad_value memory=65%
server=cache01 cpu=10% memory=15%
```

Some lines may contain malformed values (like cpu=bad_value) or missing fields.

## Task

Write a Python script that:

- Reads the `server_metrics.txt` file line by line.
- Aggregates average CPU and memory usage per server using a dictionary.
- Skips malformed lines and counts them as errors.
- Prints a summary report:
```
Server metrics summary:
web01 -> CPU: 22.5%, Memory: 37.5%
db01  -> CPU: 55.0%, Memory:70.0%
cache01 -> CPU: 10.0%, Memory: 15.0%
Malformed lines: 1
```

## Requirements / Constraints
- Use try/except to handle conversion errors (int()/float() parsing).
- Use a dictionary of lists to store CPU and memory usage per server.
- Compute average CPU and memory per server at the end.
- Ignore malformed lines but count them.