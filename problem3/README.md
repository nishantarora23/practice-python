# Problem: Web Traffic Log Analyzer

## Scenario

You are working as a DevOps engineer monitoring web server traffic. You have a log file web_traffic.txt with lines like:
```
date=2026-01-17 user=alice page=/home status=200
date=2026-01-17 user=bob page=/login status=200
date=2026-01-17 user=alice page=/profile status=404
date=2026-01-17 user=alice page=/home status=200
date=2026-01-17 user=bob page=/dashboard status=500
```

Each line has:
date
user
page visited
HTTP status code

## Task
- Write a Python script that:
- Reads the file line by line.
- Uses a nested dictionary where each user has a dictionary of pages, and each page stores a list of status codes.

Example structure:
```
traffic = {
    "alice": {
        "/home": [200, 200],
        "/profile": [404]
    },
    "bob": {
        "/login": [200],
        "/dashboard": [500]
    }
}
```

## Computes the following for each user and page:

- Total visits
- Number of successful visits (status 200)
- Number of failed visits (status not 200)
- Prints a summary report:
```
User: alice
  Page: /home -> Visits: 2, Success: 2, Fail: 0
  Page: /profile -> Visits: 1, Success: 0, Fail: 1
User: bob
  Page: /login -> Visits: 1, Success: 1, Fail: 0
  Page: /dashboard -> Visits: 1, Success: 0, Fail: 1
```

## Requirements / Challenges
- Must use a nested dictionary of lists
- Count success/fail per page
- Handle any number of users, pages, and log lines
- Practice loops inside loops, dictionary initialization, and aggregating lists