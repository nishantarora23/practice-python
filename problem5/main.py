import requests

url = "https://jsonplaceholder.typicode.com/users"
response = ""
users_by_city = {}

try:
    response = requests.request("GET", url)
    response.raise_for_status()
except Exception as e:
    print(f"Error fetching users: {e}")

if response and response.status_code == 200:
    users = response.json()
    if isinstance(users, list):
        for user in users:
            name = user['username']
            city = user['address']['city']
            users_by_city.setdefault(city, []).append(name)

for city, names in users_by_city.items():
    print(f"City: {city}")
    user_count = len(names)
    print(f"\tUsers: {user_count}")
    username = ', '.join(names)
    print(f"\tUsernames: {username}")



