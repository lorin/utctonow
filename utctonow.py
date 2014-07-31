#!/usr/bin/env python
"""utctonow

Usage:
    utctonow.py DATETIME

Convert a DATETIME in kernel log file format to local time zone.
Assumes the DATETIME is in UTC format.

Arguments:

    DATETIME    quoted datetime string in kernel log format
                e.g.: "Jul 31 13:48:34"

"""
from __future__ import print_function
from docopt import docopt

import arrow


def main(s):
    tlocal = tonow(s)
    print(tlocal.format('MMM DD YYYY HH:mm:ss ') + tlocal.tzname())


def tonow(s):
    """
    Convert a datetime string to the current time zone

    >>> tonow('Jul 31 13:48:34')
    <Arrow [2014-07-31T13:48:34+00:00]>
    """

    # the log message doesn't have year, so we prepend
    fmt = 'YYYY MMM DD HH:mm:ss'
    year = arrow.utcnow().year
    timestr = '{0} {1}'.format(year, s)
    return arrow.get(timestr, fmt).to('local')

if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments['DATETIME'])
