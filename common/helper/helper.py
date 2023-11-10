from datetime import datetime


def current_timestamps():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return timestamp


def current_date_and_time():
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return dt_string
