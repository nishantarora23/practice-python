# Problem Statement — Multi-Service Error Burst
You are monitoring logs for multiple services.

Each log entry is:
```
(timestamp, service_name, status_code)
```

Example logs:
```
logs = [
    (100, "auth", 200),
    (110, "auth", 500),
    (115, "payments", 502),
    (120, "auth", 503),
    (150, "auth", 200),
    (160, "payments", 500),
    (170, "auth", 502),
]
```

## Requirements
- Trigger an alert for a service if it has ≥ 3 errors (status_code ≥ 500) in a rolling 60-second window.
- Track multiple services independently.
- Process logs as a stream.
- Be memory-efficient (only keep recent errors).

## Expected Output
For the example above, the alert should trigger because between 110 and 120 seconds, there are 3 errors:
```
Alert triggered for <service_name>!
```