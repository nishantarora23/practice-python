from pathlib import Path
import re

pattern = re.compile(r".*user=(?P<user>\w+)\s+"
                     r"page=(?P<page>\/\w+)\s+"
                     r"status=(?P<status>\d{3})(\s+|$)")

traffic = {}

web_traffic_file = Path("./web_traffic.txt")
if web_traffic_file.is_file():
    with open(web_traffic_file, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                user = match.group("user")
                page = match.group("page")
                status = int(match.group("status"))

                traffic.setdefault(user, {})
                traffic[user].setdefault(page, [])

                traffic[user][page].append(status)

for user, pages in traffic.items():
    print(f"User: {user}")
    if pages:
        for page, status in pages.items():
            visits = len(status)
            success = status.count(200)
            fail = visits - success
            print(f"\tPage: {page} -> Visits: {visits}, Success: {success}, Fail: {fail}")
