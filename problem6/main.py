logs = [
    "INFO 2025-01-15 14:20:10 User=alice Action=Login Success",
    "ERROR 2025-01-15 14:22:31 User=admin Action=Login Failed Reason=InvalidPassword",
    "WARNING 2025-01-15 14:25:00 User=bob Action=Upload SlowNetwork",
    "ERROR 2025-01-15 14:30:45 User=alice Action=Download Failed Reason=Timeout",
    "INFO 2025-01-15 14:35:12 User=admin Action=Logout Success"
]
result = {}
fail_counter = 0
for log in logs:
    if "Failed" in log:
        fail_counter += 1
    line = log.split(" ")
    if line:
        level = line[0].lower()
        if not line[3].startswith("User="):
            break
        raw_user_info = line[3].split("=")
        if level in ["info", "error", "warning"] and len(raw_user_info) == 2 \
                and raw_user_info[0] == "User":
            user = raw_user_info[1]
            result.setdefault(level, [])
            if user not in result[level]:
                result[level].append(user)

for level, users in result.items():
    print(f"Log Level: {level.upper()}\n\tUsers: "
          f"{len(users)}\n\tUsernames: {', '.join(users)}")

print(f"\nTotal Failed Actions: {fail_counter}")

