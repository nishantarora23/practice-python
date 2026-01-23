from collections import deque

logs = [
    (100, 200),
    (110, 500),
    (115, 502),
    (120, 503),
    (150, 200),
    (160, 500),
]

WINDOW_SIZE = 60
ERROR_THRESHOLD = 3


def detect_errors(logs):
    error_window = deque()

    for timestamp, status_code in logs:
        if status_code >= 500:
            error_window.append(timestamp)

        while error_window and error_window[0] < timestamp - WINDOW_SIZE:
            error_window.popleft()

        if len(error_window) >= ERROR_THRESHOLD:
            return "Alert triggered!"


print(detect_errors(logs))