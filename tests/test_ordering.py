#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (C) 2017 David Toro <davsamirtor@gmail.com>
"""
Compatibility testing frame in python 3 and 2 for comparison fucntions

Only py2: __cmp__ = cmp = lambda (x, y): (x > y) - (x < y)

x < y calls x.__lt__(y)
x > y calls x.__gt__(y)
x <= y calls x.__le__(y)
x == y calls x.__eq__(y)
x >= y calls x.__ge__(y)
x != y and x <> y call x.__ne__(y)
"""
# compatibility with python 2 and 3
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
# http://python-future.org/compatible_idioms.html#cmp
from past.builtins import cmp

#__all__ = []
__author__ = "David Toro"
#__copyright__ = "Copyright 2017, The <name> Project"
#__credits__ = [""]
__license__ = "BSD-3-Clause"
#__version__ = "1.0.0"
__maintainer__ = "David Toro"
__email__ = "davsamirtor@gmail.com"
#__status__ = "Pre-release"

# import build-in modules
import sys
import time
# https://docs.python.org/3/library/functools.html#functools.total_ordering
from functools import total_ordering
# http://stackoverflow.com/a/33764672/5288758
from itertools import count

# import third party modules


class test_normal(object):
    order = count()

    def __init__(self, priority=0):
        self.priority = priority
        self.creation_time = time.time()
        self._creation_order = next(test_normal.order)

    def __eq__(self, other):  # complement with functools.total_ordering
        # priority comparison
        # return (self.priority,self.creation) == (other.priority,other.creation)
        # equality comparison
        return id(self) == id(other)

    def __lt__(self, other):  # complement with functools.total_ordering
        # priority comparison
        # if A is created first than B then A is expected to be less than B
        return (
            self.priority,
            self.creation_time) < (
            other.priority,
            other.creation_time)
        # return (self.priority,self._creation_order) < (other.priority,other._creation_order)
        # return (self.priority,) < (other.priority,)


@total_ordering
class test_total(test_normal):
    pass


def try_func(func):
    try:
        return func()
    except BaseException:
        return "ERROR"


def testfunc(x, y):
    """
    Apply all testing functions.

    :param A:
    :param B:
    :return:
    """
    # https://docs.python.org/2/reference/datamodel.html#object.__lt__
    # https://docs.python.org/3.6/reference/datamodel.html#object.__lt__
    # https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons
    print("Tests for x={x} and y={y}".format(x=x, y=y))
    # x < y calls x.__lt__(y)
    print("x < y:{}".format(try_func(lambda: x < y)))
    # x > y calls x.__gt__(y)
    print("x > y:{}".format(try_func(lambda: x > y)))
    # x <= y calls x.__le__(y)
    print("x <= y:{}".format(try_func(lambda: x <= y)))
    # x == y calls x.__eq__(y)
    print("x == y:{}".format(try_func(lambda: x == y)))
    # x >= y calls x.__ge__(y)
    print("x >= y:{}".format(try_func(lambda: x >= y)))
    # x != y and x <> y call x.__ne__(y)
    print("x != y:{}".format(try_func(lambda: x != y)))


if __name__ == "__main__":

    A = test_total(1)
    B = test_total(1)
    testfunc(A, B)

    A = test_normal()
    B = test_normal()
    testfunc(A, B)
