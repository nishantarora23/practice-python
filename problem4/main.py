logs = [
    "alice login success",
    "bob login failed",
    "alice logout success",
    "alice login success",
    "bob login success",
    "carol login failed",
    "carol login failed"
]
logger = {}

for log_line in logs:
    line_split = log_line.split(" ")
    user, action, status = log_line.split()

    logger.setdefault(user, {})
    logger[user].setdefault(action, [])
    logger[user][action].append(status)

for user, actions in logger.items():
    print(f"User: {user}")

    for action, status in actions.items():
        total = len(status)
        success = status.count("success")
        failed = total - success
        print(f"\t{action} -> Total: {total}, Success: {success}, Fail: {failed}")
