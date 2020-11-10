import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)

print(randomDate("2001-1-1", "2001-12-31", random.random()))
print(randomDate("2002-1-1", "2002-12-31", random.random()))
print(randomDate("2003-1-1", "2003-12-31", random.random()))
print(randomDate("2004-1-1", "2004-12-31", random.random()))