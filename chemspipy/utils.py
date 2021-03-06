# -*- coding: utf-8 -*-
"""
chemspipy.utils
~~~~~~~~~~~~~~~

Miscellaneous utility functions.

:copyright: Copyright 2014 by Matt Swain.
:license: MIT, see LICENSE file for more details.
"""




import datetime
import functools


def memoized_property(fget):
    """Decorator to create memoized properties."""
    attr_name = '_{}'.format(fget.__name__)

    @functools.wraps(fget)
    def fget_memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fget(self))
        return getattr(self, attr_name)
    return property(fget_memoized)


def timestamp(ts):
    """Create a datetime object from a timestamp string."""
    fmt = '%Y-%m-%dT%H:%M:%S.%f' if '.' in ts else '%Y-%m-%dT%H:%M:%S'
    return datetime.datetime.strptime(ts, fmt)


def duration(ts):
    """Create a timedelta object from a duration string."""
    fmt = '%H:%M:%S.%f' if '.' in ts else '%H:%M:%S'
    dt = datetime.datetime.strptime(ts, fmt)
    return datetime.timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second, microseconds=dt.microsecond)
