# Problem: Log Line Analyzer (String-Focused)

## Scenario
You are given a list of raw log lines collected from a server.
Each log line is a single string.

Example log line:
```
"ERROR 2025-01-15 14:22:31 User=admin Action=Login Failed Reason=InvalidPassword"
```

## Input
You are given a list of strings:
```
logs = [
    "INFO 2025-01-15 14:20:10 User=alice Action=Login Success",
    "ERROR 2025-01-15 14:22:31 User=admin Action=Login Failed Reason=InvalidPassword",
    "WARNING 2025-01-15 14:25:00 User=bob Action=Upload SlowNetwork",
    "ERROR 2025-01-15 14:30:45 User=alice Action=Download Failed Reason=Timeout",
    "INFO 2025-01-15 14:35:12 User=admin Action=Logout Success"
]
```

## Your Tasks
1. Extract Log Level 
    - From each log line:
    - Extract the log level (INFO, ERROR, WARNING)
    - Convert it to uppercase (even if already uppercase)

2. Extract Username
    - Extract the username after User= 
    - Store usernames as lowercase strings

3. Detect Failed Actions 
    - A log is considered failed if the word "Failed" appears anywhere in the string
    - Count how many failures occurred

4. Build a Summary Dictionary 
    - Avoid duplicate usernames per level
    - Create a dictionary like this:
  ```
  summary = {
      "info": ["alice", "admin"],
      "warning": ["bob"],
      "error": ["admin", "alice"]
  }


  Where:
  Key → lowercase log level
  Value → list of usernames that appeared in that log level
  ```

5. Print a Report

Expected output format:
```
Log Level: INFO
  Users: 2
  Usernames: alice, admin

Log Level: WARNING
  Users: 1
  Usernames: bob

Log Level: ERROR
  Users: 2
  Usernames: admin, alice

Total Failed Actions: 2
```

## Rules
- No regex
- No file handling
- Use only string methods
- Use lists & dictionaries
- Case normalization is required
