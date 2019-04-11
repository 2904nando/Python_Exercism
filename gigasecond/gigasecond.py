import datetime

def add_gigasecond(moment):
    return moment + datetime.timedelta(seconds=10**9)
