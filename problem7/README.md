# Problem Statement — Single-Service Error Burst

You are monitoring logs for a single service.
Each log entry is:
```
(timestamp, status_code)
```

Example:
```
logs = [
    (100, 200),
    (110, 500),
    (115, 502),
    (120, 503),
    (150, 200),
    (160, 500),
]
```

##  Requirements
- Trigger an alert if there are ≥ 3 errors (status_code ≥ 500) in any rolling 60-second window.
- Process logs as a stream.
- Use deque to maintain the sliding window.

## Expected Output
For the example above, the alert should trigger because between 110 and 120 seconds, there are 3 errors:
```
Alert triggered!
```