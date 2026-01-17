# Problem: Automated Log Sanitizer & Reporter
## Scenario

You are a DevOps engineer. Your application generates log files that contain:

IP addresses
Usernames
Passwords
Timestamps

## Example log file (app_logs.txt):
```
2026-01-17 10:23:45 user=alice ip=192.168.1.10 password=MySecret123 action=login
2026-01-17 10:25:12 user=bob ip=10.0.0.5 password=pa55word! action=logout
2026-01-17 10:30:01 user=carol ip=172.16.0.3 password=HelloWorld action=login
```

## Your Task

- Write a Python script that:
- Reads the log file line by line.
- Sanitizes sensitive data:
- Mask passwords (e.g., replace with *****)
- Mask IP addresses (replace with X.X.X.X)
- Counts login attempts per user and stores in a dictionary.
- Writes the sanitized logs to a new file sanitized_logs.txt.
- Prints a summary report:
```
Login summary:
alice: 1 login(s)
bob: 0 login(s)
carol: 1 login(s)
```