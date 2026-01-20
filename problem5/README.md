# Problem: API Data Fetcher & Analyzer
## Scenario

You are working with a public API that returns JSON data about users.
Your task is to fetch the data, process it, and generate a summary.

You will use this API endpoint:

`https://jsonplaceholder.typicode.com/users`


This API returns a JSON list of users like:
```
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "leanne@example.com",
    "address": {
      "city": "Gwenborough"
    }
  }
]
```

## Your Tasks
- Fetch Data from API
- Use the requests module
- Make a GET request to the API
- Handle HTTP errors properly
- Parse JSON Response
- Use the json module (or response.json())
- Convert API response into Python data structures

## Build a Summary Dictionary

Create a dictionary like this:
```
users_by_city = {
    "Gwenborough": ["Bret", "Antonette"],
    "Wisokyburgh": ["Samantha"],
}
```

Where:
Key → City name
Value → List of usernames living in that city

## Print a Report
```
City: Gwenborough
  Users: 2
  Usernames: Bret, Antonette

City: Wisokyburgh
  Users: 1
  Usernames: Samantha
```

## Rules
- Must use requests
- Must use json or response.json()
- No file handling
- No regex
- Use lists and dictionaries