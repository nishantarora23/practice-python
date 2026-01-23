from collections import deque

WINDOW_SIZE = 60
ERROR_THRESHOLD = 3

logs = [
    (100, "auth", 200),
    (110, "auth", 500),
    (115, "payments", 502),
    (120, "auth", 503),
    (150, "auth", 200),
    (160, "payments", 500),
    (170, "auth", 502),
]


def detect_errors(logs):
    service_info = {}
    for timestamp, service, status in logs:

        service_info.setdefault(service, deque())
        if status >= 500:
            service_info[service].append(timestamp)

        while service_info[service] and service_info[service][0] < timestamp - WINDOW_SIZE:
            service_info[service].popleft()

        if len(service_info[service]) >= ERROR_THRESHOLD:
            return f"Alert triggered for {service} at {timestamp}."


print(detect_errors(logs))
