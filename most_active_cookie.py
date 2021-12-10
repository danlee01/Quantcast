"""
most_active_cookie is a command line program that prints 
the most active cookie(s) in a log on a given day. 
We define the most active cookie as one seen the most on a given day
"""
import argparse
import logging

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("cookie_log", help="cookie file to be searched")
    parser.add_argument("-d", "--date", type=str, help="date in UTC.")
    args = parser.parse_args()
    return args

def get_cookie(log):
    """Return the cookie of a given log"""
    try:
        cookie, _ = log
    except ValueError:
        logging.debug("Tuple unpacking failed inside get_cookie. log: {}".format(log))
        cookie = None

    return cookie


def get_timestamp(log):
    """Return the timestamp of a given log"""
    try:
        _, timestamp = log
        date, time = timestamp.strip().split("T")
    except ValueError:
        logging.debug("Tuple unpacking failed inside get_timestamp. log: {}".format(log))
        date, time = None, None

    return date, time


def get_most_recent_timestamp(logs, target_date=None):
    """Returns the timestamp of the most recent cookie as for given date.
    Assumes that the logs are sorted by timestamp.
    This will be -1 if there are no cookies.
    """
    if not logs:
        return None, None

    try:
        if not target_date:
            date, time = get_timestamp(logs[0])
        else:
            for log in logs:
                date, time = get_timestamp(log)
                if date == target_date:
                    break
    except ValueError:
        logging.debug("Tuple unpacking failed inside get_most_recent_timestamp. log: {}".format(log))
        date, time = None, None
    return date, time


def most_active_cookie(log, target_date=None):
    """Returns the most active cookie(s) during a given day.
    If a date is not given, uses the most recent day in the log.
    """
    try:
        cookie_log = open(log, "r")
    except IOError:
        logging.debug("cookie_log could not be opened.")
        return
    
    logs = [log.split(",") for log in cookie_log]

    if not target_date:
        target_date, _ = get_most_recent_timestamp(logs)
        logging.debug("User did not provide -d. Default to most recent day: {}".format(target_date))

    cookie_counter = {}
    for log in logs:
        cookie = get_cookie(log)
        date, _ = get_timestamp(log)
        if date == target_date:
            if cookie not in cookie_counter:
                cookie_counter[cookie] = 0
            cookie_counter[cookie] += 1

    max_occurrances = max(cookie_counter.values())
    most_active = []
    for cookie in cookie_counter.keys():
        if cookie_counter[cookie] == max_occurrances:
            most_active.append(cookie)

    for cookie in most_active:
        print(cookie)


if __name__ == "__main__":
    args = parse_args()

    logging.basicConfig(filename="most_active_cookie.log", \
                        format='%(levelname)s: %(message)s', \
                        filemode='w+', level=logging.DEBUG) 

    logging.basicConfig(filename="most_active_cookie.log", \
                        format='%(levelname)s: %(message)s', \
                        filemode='w+', level=logging.DEBUG) 

    most_active_cookie(args.cookie_log, args.date)