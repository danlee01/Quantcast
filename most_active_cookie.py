"""
This is my solution for Quantcase

will need:
    https://github.com/danlee01/STEM-Center/blob/master/STEMCenterProject.py
    https://docs.python.org/3/howto/argparse.html
    https://en.wikipedia.org/wiki/HTTP_cookie


log.strip().split(",") -> decompose(log) ?
"""
import argparse
import logging
#                                                                             |
def get_most_recent_timestamp(logs, target_date=None):
    """Returns the timestamp of the most recent cookie as for given date.
    Assumes that the logs are sorted by timestamp.
    This will be -1 if there are no cookies.
    """
    if not logs:
        return -1  # ??
    
    if not target_date:
        _, timestamp = logs[0]
        date, time = timestamp.strip().split("T")
        return date, time
    else:
        for log in logs:
            _, timestamp = log.split(",")
            date, time = timestamp.strip().split("T")
            if date == target_date:
                return date, time
    
    return -1


def most_active_cookie(log, target_date):
    """Returns the most active cookie(s) during a given day.
    If a date is not given, uses the most recent day in the log.
    """

    try:
        cookie_log = open(log, "r")
    except IOError:
        return
    
    most_active_cookie = []
    # I have enough memory to read in the entire file
    logs = [log.split(",") for log in cookie_log]
    
    

    if not target_date:
        target_date, target_time = get_most_recent_timestamp(logs)
        print(f"date: {target_date}, time: {target_time}")
    else:
        print("hi")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cookie_log", help="cookie file to be searched")
    parser.add_argument("-d", "--date", type=str, help="date in UTC.")
    args = parser.parse_args()

    most_active_cookie(args.cookie_log, args.date)