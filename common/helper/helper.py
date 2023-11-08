from datetime import datetime


def current_timestamps():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return timestamp
