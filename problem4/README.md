# Problem: User Activity Analyzer (Core Python Only)

## Scenario
You are given a list of user activity strings coming from an application:
```
logs = [
    "alice login success",
    "bob login failed",
    "alice logout success",
    "alice login success",
    "bob login success",
    "carol login failed",
    "carol login failed"
]
```

Each log entry has:
`<user> <action> <status>`

## Your Tasks
- Build a dictionary with this structure:
```
activity = {
    "alice": {
        "login": ["success", "success"],
        "logout": ["success"]
    },
    "bob": {
        "login": ["failed", "success"]
    },
    "carol": {
        "login": ["failed", "failed"]
    }
}
```

- Using the dictionary, print a summary:
```
User: alice
  login -> total: 2, success: 2, failed: 0
  logout -> total: 1, success: 1, failed: 0

User: bob
  login -> total: 2, success: 1, failed: 1

User: carol
  login -> total: 2, success: 0, failed: 2
```

## Rules
- No regex
- No file handling
- No imports
- Use only:
    - split()
    - lists
    - dictionaries
    - loops
    - conditionals