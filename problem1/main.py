from pathlib import Path
import re

log_file = Path("./app_logs.txt")
masked_lines = []
login_attempts = {}
ip_mask_pattern = r"(\d+\.){3}\d+"
password_mask_pattern = r"password=.*?(?=\s|$)"

if log_file.is_file():
    with open(f"{log_file}", "r") as lines:
        for line in lines:
            updated_line = re.sub(ip_mask_pattern, "X.X.X.X", line)
            updated_line = re.sub(password_mask_pattern, "password=*****", updated_line)
            masked_lines.append(updated_line)
            user_match = re.search(r"user=(\w+)", line)
            user = ""
            if user_match:
                user = user_match.group(1)
            if 'action=login' in line and user:
                login_attempts[user] = login_attempts.get(user, 0) + 1
            else:
                login_attempts.setdefault(user, 0)

    with open(f"./sanitized_logs.txt", "w") as f:
        if masked_lines:
            f.writelines(masked_lines)
        else:
            print(f"There are no masked lines.")

    print("Login summary:")
    for user, count in login_attempts.items():
        print(f"{user}: {count} login(s)")