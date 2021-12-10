"""
most_active_cookie is a command line program that prints the most active cookie(s) in a log on a given day. 
We define the most active cookie as one seen the most on a given day
"""
import argparse
import logging
             
def get_cookie(log):
    """Return the cookie of a given log"""
    cookie, _ = log
    return cookie
def get_timestamp(log):
    """Return the timestamp of a given log"""
    if not log:
        return log
    
    _, timestamp = log
    date, time = timestamp.strip().split("T")

    return date, time

def get_most_recent_timestamp(logs, target_date=None):
    """Returns the timestamp of the most recent cookie as for given date.
    Assumes that the logs are sorted by timestamp.
    This will be -1 if there are no cookies.
    """
    if not logs:
        return -1  # ??
    
    if not target_date:
        date, time = get_timestamp(logs[0])
        return date, time
    else:
        for log in logs:
            date, time = get_timestamp(log)
            if date == target_date:
                return date, time
    
    return -1



def most_active_cookie(log, target_date=None):
    """Returns the most active cookie(s) during a given day.
    If a date is not given, uses the most recent day in the log.
    """

    try:
        cookie_log = open(log, "r")
    except IOError:
        return
    
    logs = [log.split(",") for log in cookie_log]

    if not target_date:
        target_date, _ = get_most_recent_timestamp(logs)

    cookie_counter = {}
    for log in logs:
        cookie = get_cookie(log)
        date, _ = get_timestamp(log)
        if date == target_date:
            if cookie not in cookie_counter:
                cookie_counter[cookie] = 0
            cookie_counter[cookie] += 1

    max_occurrances = max(cookie_counter.values())
    most_active_cookies = [cookie for cookie in cookie_counter.keys() if cookie_counter[cookie] == max_occurrances]

    for cookie in most_active_cookies:
        print(cookie)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cookie_log", help="cookie file to be searched")
    parser.add_argument("-d", "--date", type=str, help="date in UTC.")
    args = parser.parse_args()

    most_active_cookie(args.cookie_log, args.date)