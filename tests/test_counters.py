#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (C) 2017 David Toro <davsamirtor@gmail.com>
"""

"""
# compatibility with python 2 and 3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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

# import third party modules
from sutils.counters import *

if __name__ == "__main__" and False:
    b = DigitCounter(3)
    b.letter = "b"
    a = DigitCounter(2, b)
    a.letter = "a"

    for i in a:
        print("state: ", i.get_state())
        print("state is valid: ", bool(i))
        print("state Train: ", i.get_state_train(), a, b)

if __name__ == "__main__" and True:
    # Test frames to ground truth information to validate Counters
    """
    max 2,3,4,5
    -0 [0, 0, 0, 0] --> 0
    -1 [1, 0, 0, 0] --> 1*2â° = 1
    -2 [0, 1, 0, 0] --> 2*1 = 2
    3 [1, 1, 0, 0] --> 1*2â° + 2*1 = 3
    -4 [0, 2, 0, 0] --> 2*2 = 4
    5 [1, 2, 0, 0] --> 1*2â° + 2*2 = 5
    -6 [0, 0, 1, 0] --> 2*3*1 = 6
    7 [1, 0, 1, 0] --> 1 + 2*3*1 = 7
    8 [0, 1, 1, 0] --> 2*1 + 2*3*1 = 8
    9 [1, 1, 1, 0] --> 1 + 2*1 + 2*3*1 = 9
    """
    import time

    def getLetter(array):
        return [item.letter for item in array]

    test = (
        "set",
        "set_state",
        "order",
        "timeTest",
        "counterTest",
        "Iterations")
    #tests = ("Iterations")

    cmp_values = [[0, 0, 0, 0],
                  [1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0], [1, 2, 0, 0],
                  [0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 0], [0, 2, 1, 0],
                  [1, 2, 1, 0], [0, 0, 2, 0], [1, 0, 2, 0], [0, 1, 2, 0], [1, 1, 2, 0],
                  [0, 2, 2, 0], [1, 2, 2, 0], [0, 0, 3, 0], [1, 0, 3, 0], [0, 1, 3, 0],
                  [1, 1, 3, 0], [0, 2, 3, 0], [1, 2, 3, 0], [0, 0, 0, 1], [1, 0, 0, 1],
                  [0, 1, 0, 1], [1, 1, 0, 1], [0, 2, 0, 1], [1, 2, 0, 1], [0, 0, 1, 1],
                  [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 2, 1, 1], [1, 2, 1, 1],
                  [0, 0, 2, 1], [1, 0, 2, 1], [0, 1, 2, 1], [1, 1, 2, 1], [0, 2, 2, 1],
                  [1, 2, 2, 1], [0, 0, 3, 1], [1, 0, 3, 1], [0, 1, 3, 1], [1, 1, 3, 1],
                  [0, 2, 3, 1], [1, 2, 3, 1], [0, 0, 0, 2], [1, 0, 0, 2], [0, 1, 0, 2],
                  [1, 1, 0, 2], [0, 2, 0, 2], [1, 2, 0, 2], [0, 0, 1, 2], [1, 0, 1, 2],
                  [0, 1, 1, 2], [1, 1, 1, 2], [0, 2, 1, 2], [1, 2, 1, 2], [0, 0, 2, 2],
                  [1, 0, 2, 2], [0, 1, 2, 2], [1, 1, 2, 2], [0, 2, 2, 2], [1, 2, 2, 2],
                  [0, 0, 3, 2], [1, 0, 3, 2], [0, 1, 3, 2], [1, 1, 3, 2], [0, 2, 3, 2],
                  [1, 2, 3, 2], [0, 0, 0, 3], [1, 0, 0, 3], [0, 1, 0, 3], [1, 1, 0, 3],
                  [0, 2, 0, 3], [1, 2, 0, 3], [0, 0, 1, 3], [1, 0, 1, 3], [0, 1, 1, 3],
                  [1, 1, 1, 3], [0, 2, 1, 3], [1, 2, 1, 3], [0, 0, 2, 3], [1, 0, 2, 3],
                  [0, 1, 2, 3], [1, 1, 2, 3], [0, 2, 2, 3], [1, 2, 2, 3], [0, 0, 3, 3],
                  [1, 0, 3, 3], [0, 1, 3, 3], [1, 1, 3, 3], [0, 2, 3, 3], [1, 2, 3, 3],
                  [0, 0, 0, 4], [1, 0, 0, 4], [0, 1, 0, 4], [1, 1, 0, 4], [0, 2, 0, 4],
                  [1, 2, 0, 4], [0, 0, 1, 4], [1, 0, 1, 4], [0, 1, 1, 4], [1, 1, 1, 4],
                  [0, 2, 1, 4], [1, 2, 1, 4], [0, 0, 2, 4], [1, 0, 2, 4], [0, 1, 2, 4],
                  [1, 1, 2, 4], [0, 2, 2, 4], [1, 2, 2, 4], [0, 0, 3, 4], [1, 0, 3, 4],
                  [0, 1, 3, 4], [1, 1, 3, 4], [0, 2, 3, 4], [1, 2, 3, 4]]

    a, b, c, d, clist, clist_inv, cset = None, None, None, None, None, None, None

    def init_counters(values=(1, 2, 3, 4)):
        global a, b, c, d, clist, clist_inv, cset
        d = DigitCounter(5)
        d.letter = "d"
        c = DigitCounter(4, d)
        c.letter = "c"
        b = DigitCounter(3, c)
        b.letter = "b"
        a = DigitCounter(2, b)
        a.letter = "a"
        a.set_state_train(values)
        clist = a.get_counter_train()  # a is master
        clist_inv = clist[::-1]
        cset = MechanicalCounter(clist)

    init_counters()

    if "set" in test:
        """
        Test the different orders that MechanicalCounter can take. Here the
        states are each individual counter state, the real order are the phisical
        order that the counters take in the object in self.train and Virtual order
        the ones specified by self.order which refers to the links each counter
        has with the other. There is the normal count, for the initial count. The
        inverted link using self.invert_link_order(). Inverted count using
        self.invert_count flag. The inverted ranks using self.invert_ranks().
        And the inverted real order using self.invert_real_order()
        """
        init_counters((0, 0, 0, 0))
        cset = MechanicalCounter(clist)
        print("Normal")
        print("States order", cset.order)
        assert cset.order == [0, 1, 2, 3]  # values should be set the same
        print("Real order:", getLetter(clist))
        assert getLetter(cset.get_real_counter_train()) == [
            'a', 'b', 'c', 'd']  # real order is the same
        print("Virtual order", getLetter(cset.master.get_counter_train()))
        assert getLetter(cset.get_counter_train()) == [
            'a', 'b', 'c', 'd']  # virtual order is the same
        assert [i for i in cset] == cmp_values  # permutes the same
        #cset.stopped = False
        for i in cset:
            print(i)

        print("Inverted link")
        cset = MechanicalCounter(clist)
        cset.reset()
        cset.invert_link_order()

        print("States order", cset.order)
        assert cset.order == [3, 2, 1, 0]

        print("Real order:", getLetter(cset.get_real_counter_train()))
        assert getLetter(cset.get_real_counter_train()) == [
            'a', 'b', 'c', 'd']  # real order is the same

        print("Virtual order", getLetter(cset.master.get_counter_train()))
        assert getLetter(cset.get_counter_train()) == [
            'd', 'c', 'b', 'a']  # virtual order is the same

        cmp_values_inv_link = [[0, 0, 0, 0],
                               [0, 0, 0, 1], [0, 0, 0, 2], [0, 0, 0, 3], [0, 0, 0, 4], [0, 0, 1, 0],
                               [0, 0, 1, 1], [0, 0, 1, 2], [0, 0, 1, 3], [0, 0, 1, 4], [0, 0, 2, 0],
                               [0, 0, 2, 1], [0, 0, 2, 2], [0, 0, 2, 3], [0, 0, 2, 4], [0, 0, 3, 0],
                               [0, 0, 3, 1], [0, 0, 3, 2], [0, 0, 3, 3], [0, 0, 3, 4], [0, 1, 0, 0],
                               [0, 1, 0, 1], [0, 1, 0, 2], [0, 1, 0, 3], [0, 1, 0, 4], [0, 1, 1, 0],
                               [0, 1, 1, 1], [0, 1, 1, 2], [0, 1, 1, 3], [0, 1, 1, 4], [0, 1, 2, 0],
                               [0, 1, 2, 1], [0, 1, 2, 2], [0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 3, 0],
                               [0, 1, 3, 1], [0, 1, 3, 2], [0, 1, 3, 3], [0, 1, 3, 4], [0, 2, 0, 0],
                               [0, 2, 0, 1], [0, 2, 0, 2], [0, 2, 0, 3], [0, 2, 0, 4], [0, 2, 1, 0],
                               [0, 2, 1, 1], [0, 2, 1, 2], [0, 2, 1, 3], [0, 2, 1, 4], [0, 2, 2, 0],
                               [0, 2, 2, 1], [0, 2, 2, 2], [0, 2, 2, 3], [0, 2, 2, 4], [0, 2, 3, 0],
                               [0, 2, 3, 1], [0, 2, 3, 2], [0, 2, 3, 3], [0, 2, 3, 4], [1, 0, 0, 0],
                               [1, 0, 0, 1], [1, 0, 0, 2], [1, 0, 0, 3], [1, 0, 0, 4], [1, 0, 1, 0],
                               [1, 0, 1, 1], [1, 0, 1, 2], [1, 0, 1, 3], [1, 0, 1, 4], [1, 0, 2, 0],
                               [1, 0, 2, 1], [1, 0, 2, 2], [1, 0, 2, 3], [1, 0, 2, 4], [1, 0, 3, 0],
                               [1, 0, 3, 1], [1, 0, 3, 2], [1, 0, 3, 3], [1, 0, 3, 4], [1, 1, 0, 0],
                               [1, 1, 0, 1], [1, 1, 0, 2], [1, 1, 0, 3], [1, 1, 0, 4], [1, 1, 1, 0],
                               [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 1, 4], [1, 1, 2, 0],
                               [1, 1, 2, 1], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 2, 4], [1, 1, 3, 0],
                               [1, 1, 3, 1], [1, 1, 3, 2], [1, 1, 3, 3], [1, 1, 3, 4], [1, 2, 0, 0],
                               [1, 2, 0, 1], [1, 2, 0, 2], [1, 2, 0, 3], [1, 2, 0, 4], [1, 2, 1, 0],
                               [1, 2, 1, 1], [1, 2, 1, 2], [1, 2, 1, 3], [1, 2, 1, 4], [1, 2, 2, 0],
                               [1, 2, 2, 1], [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 2, 4], [1, 2, 3, 0],
                               [1, 2, 3, 1], [1, 2, 3, 2], [1, 2, 3, 3], [1, 2, 3, 4]]

        assert [i for i in cset] == cmp_values_inv_link  # permutes the same
        #cset.stopped = False
        for i in cset:
            print(i)

        print("Inverted count")
        cset = MechanicalCounter(clist)
        cset.reset()
        cset.invert_count = True

        print("States order", cset.order)
        assert cset.order == [0, 1, 2, 3]  # values should be set the same

        print("Real order:", getLetter(cset.get_real_counter_train()))
        assert getLetter(cset.get_real_counter_train()) == [
            'a', 'b', 'c', 'd']  # real order is the same

        print("Virtual order", getLetter(cset.get_counter_train()))
        assert getLetter(cset.get_counter_train()) == [
            'a', 'b', 'c', 'd']  # real order is the same

        cmp_values_inv_count = [[1, 2, 3, 4],
                                [0, 2, 3, 4], [1, 1, 3, 4], [0, 1, 3, 4], [1, 0, 3, 4], [0, 0, 3, 4],
                                [1, 2, 2, 4], [0, 2, 2, 4], [1, 1, 2, 4], [0, 1, 2, 4], [1, 0, 2, 4],
                                [0, 0, 2, 4], [1, 2, 1, 4], [0, 2, 1, 4], [1, 1, 1, 4], [0, 1, 1, 4],
                                [1, 0, 1, 4], [0, 0, 1, 4], [1, 2, 0, 4], [0, 2, 0, 4], [1, 1, 0, 4],
                                [0, 1, 0, 4], [1, 0, 0, 4], [0, 0, 0, 4], [1, 2, 3, 3], [0, 2, 3, 3],
                                [1, 1, 3, 3], [0, 1, 3, 3], [1, 0, 3, 3], [0, 0, 3, 3], [1, 2, 2, 3],
                                [0, 2, 2, 3], [1, 1, 2, 3], [0, 1, 2, 3], [1, 0, 2, 3], [0, 0, 2, 3],
                                [1, 2, 1, 3], [0, 2, 1, 3], [1, 1, 1, 3], [0, 1, 1, 3], [1, 0, 1, 3],
                                [0, 0, 1, 3], [1, 2, 0, 3], [0, 2, 0, 3], [1, 1, 0, 3], [0, 1, 0, 3],
                                [1, 0, 0, 3], [0, 0, 0, 3], [1, 2, 3, 2], [0, 2, 3, 2], [1, 1, 3, 2],
                                [0, 1, 3, 2], [1, 0, 3, 2], [0, 0, 3, 2], [1, 2, 2, 2], [0, 2, 2, 2],
                                [1, 1, 2, 2], [0, 1, 2, 2], [1, 0, 2, 2], [0, 0, 2, 2], [1, 2, 1, 2],
                                [0, 2, 1, 2], [1, 1, 1, 2], [0, 1, 1, 2], [1, 0, 1, 2], [0, 0, 1, 2],
                                [1, 2, 0, 2], [0, 2, 0, 2], [1, 1, 0, 2], [0, 1, 0, 2], [1, 0, 0, 2],
                                [0, 0, 0, 2], [1, 2, 3, 1], [0, 2, 3, 1], [1, 1, 3, 1], [0, 1, 3, 1],
                                [1, 0, 3, 1], [0, 0, 3, 1], [1, 2, 2, 1], [0, 2, 2, 1], [1, 1, 2, 1],
                                [0, 1, 2, 1], [1, 0, 2, 1], [0, 0, 2, 1], [1, 2, 1, 1], [0, 2, 1, 1],
                                [1, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [0, 0, 1, 1], [1, 2, 0, 1],
                                [0, 2, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1],
                                [1, 2, 3, 0], [0, 2, 3, 0], [1, 1, 3, 0], [0, 1, 3, 0], [1, 0, 3, 0],
                                [0, 0, 3, 0], [1, 2, 2, 0], [0, 2, 2, 0], [1, 1, 2, 0], [0, 1, 2, 0],
                                [1, 0, 2, 0], [0, 0, 2, 0], [1, 2, 1, 0], [0, 2, 1, 0], [1, 1, 1, 0],
                                [0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 0], [1, 2, 0, 0], [0, 2, 0, 0],
                                [1, 1, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]

        # a.invert_count = True
        # [i.get_state_train() for i in a]
        val = [i for i in cset]
        assert val == cmp_values_inv_count  # permutes the same
        #cset.stopped = False
        for i in cset:
            print(i)

        print("Inverted ranks")
        cset = MechanicalCounter(clist)
        cset.reset()
        cset.invert_ranks()

        print("States order", cset.order)
        assert cset.order == [3, 2, 1, 0]

        print("Real order:", getLetter(cset.get_real_counter_train()))
        assert getLetter(cset.get_real_counter_train()) == [
            'a', 'b', 'c', 'd']  # real order is the same

        print("Virtual order", getLetter(cset.get_counter_train()))
        assert getLetter(cset.get_counter_train()) == [
            'd', 'c', 'b', 'a']  # real order is the same

        cmp_values_inv_ranks = [[0, 0, 0, 0],
                                [0, 0, 0, 1], [0, 0, 0, 2], [0, 0, 0, 3], [0, 0, 0, 4], [0, 0, 1, 0],
                                [0, 0, 1, 1], [0, 0, 1, 2], [0, 0, 1, 3], [0, 0, 1, 4], [0, 0, 2, 0],
                                [0, 0, 2, 1], [0, 0, 2, 2], [0, 0, 2, 3], [0, 0, 2, 4], [0, 0, 3, 0],
                                [0, 0, 3, 1], [0, 0, 3, 2], [0, 0, 3, 3], [0, 0, 3, 4], [0, 1, 0, 0],
                                [0, 1, 0, 1], [0, 1, 0, 2], [0, 1, 0, 3], [0, 1, 0, 4], [0, 1, 1, 0],
                                [0, 1, 1, 1], [0, 1, 1, 2], [0, 1, 1, 3], [0, 1, 1, 4], [0, 1, 2, 0],
                                [0, 1, 2, 1], [0, 1, 2, 2], [0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 3, 0],
                                [0, 1, 3, 1], [0, 1, 3, 2], [0, 1, 3, 3], [0, 1, 3, 4], [0, 2, 0, 0],
                                [0, 2, 0, 1], [0, 2, 0, 2], [0, 2, 0, 3], [0, 2, 0, 4], [0, 2, 1, 0],
                                [0, 2, 1, 1], [0, 2, 1, 2], [0, 2, 1, 3], [0, 2, 1, 4], [0, 2, 2, 0],
                                [0, 2, 2, 1], [0, 2, 2, 2], [0, 2, 2, 3], [0, 2, 2, 4], [0, 2, 3, 0],
                                [0, 2, 3, 1], [0, 2, 3, 2], [0, 2, 3, 3], [0, 2, 3, 4], [1, 0, 0, 0],
                                [1, 0, 0, 1], [1, 0, 0, 2], [1, 0, 0, 3], [1, 0, 0, 4], [1, 0, 1, 0],
                                [1, 0, 1, 1], [1, 0, 1, 2], [1, 0, 1, 3], [1, 0, 1, 4], [1, 0, 2, 0],
                                [1, 0, 2, 1], [1, 0, 2, 2], [1, 0, 2, 3], [1, 0, 2, 4], [1, 0, 3, 0],
                                [1, 0, 3, 1], [1, 0, 3, 2], [1, 0, 3, 3], [1, 0, 3, 4], [1, 1, 0, 0],
                                [1, 1, 0, 1], [1, 1, 0, 2], [1, 1, 0, 3], [1, 1, 0, 4], [1, 1, 1, 0],
                                [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 1, 4], [1, 1, 2, 0],
                                [1, 1, 2, 1], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 2, 4], [1, 1, 3, 0],
                                [1, 1, 3, 1], [1, 1, 3, 2], [1, 1, 3, 3], [1, 1, 3, 4], [1, 2, 0, 0],
                                [1, 2, 0, 1], [1, 2, 0, 2], [1, 2, 0, 3], [1, 2, 0, 4], [1, 2, 1, 0],
                                [1, 2, 1, 1], [1, 2, 1, 2], [1, 2, 1, 3], [1, 2, 1, 4], [1, 2, 2, 0],
                                [1, 2, 2, 1], [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 2, 4], [1, 2, 3, 0],
                                [1, 2, 3, 1], [1, 2, 3, 2], [1, 2, 3, 3], [1, 2, 3, 4]]

        assert [i for i in cset] == cmp_values_inv_ranks  # permutes the same
        #cset.stopped = False
        for i in cset:
            print(i)

        print("Inverted real order")
        cset = MechanicalCounter(clist)
        cset.reset()
        cset.invert_real_order()

        print("States order", cset.order)
        assert cset.order == [0, 1, 2, 3]

        print("Real order:", getLetter(cset.get_real_counter_train()))
        assert getLetter(cset.get_real_counter_train()) == [
            'd', 'c', 'b', 'a']  # real order is the same

        print("Virtual order", getLetter(cset.master.get_counter_train()))
        assert getLetter(cset.get_counter_train()) == [
            'd', 'c', 'b', 'a']  # real order is the same

        cmp_values_inv_real = [[0, 0, 0, 0],
                               [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0], [0, 1, 0, 0],
                               [1, 1, 0, 0], [2, 1, 0, 0], [3, 1, 0, 0], [4, 1, 0, 0], [0, 2, 0, 0],
                               [1, 2, 0, 0], [2, 2, 0, 0], [3, 2, 0, 0], [4, 2, 0, 0], [0, 3, 0, 0],
                               [1, 3, 0, 0], [2, 3, 0, 0], [3, 3, 0, 0], [4, 3, 0, 0], [0, 0, 1, 0],
                               [1, 0, 1, 0], [2, 0, 1, 0], [3, 0, 1, 0], [4, 0, 1, 0], [0, 1, 1, 0],
                               [1, 1, 1, 0], [2, 1, 1, 0], [3, 1, 1, 0], [4, 1, 1, 0], [0, 2, 1, 0],
                               [1, 2, 1, 0], [2, 2, 1, 0], [3, 2, 1, 0], [4, 2, 1, 0], [0, 3, 1, 0],
                               [1, 3, 1, 0], [2, 3, 1, 0], [3, 3, 1, 0], [4, 3, 1, 0], [0, 0, 2, 0],
                               [1, 0, 2, 0], [2, 0, 2, 0], [3, 0, 2, 0], [4, 0, 2, 0], [0, 1, 2, 0],
                               [1, 1, 2, 0], [2, 1, 2, 0], [3, 1, 2, 0], [4, 1, 2, 0], [0, 2, 2, 0],
                               [1, 2, 2, 0], [2, 2, 2, 0], [3, 2, 2, 0], [4, 2, 2, 0], [0, 3, 2, 0],
                               [1, 3, 2, 0], [2, 3, 2, 0], [3, 3, 2, 0], [4, 3, 2, 0], [0, 0, 0, 1],
                               [1, 0, 0, 1], [2, 0, 0, 1], [3, 0, 0, 1], [4, 0, 0, 1], [0, 1, 0, 1],
                               [1, 1, 0, 1], [2, 1, 0, 1], [3, 1, 0, 1], [4, 1, 0, 1], [0, 2, 0, 1],
                               [1, 2, 0, 1], [2, 2, 0, 1], [3, 2, 0, 1], [4, 2, 0, 1], [0, 3, 0, 1],
                               [1, 3, 0, 1], [2, 3, 0, 1], [3, 3, 0, 1], [4, 3, 0, 1], [0, 0, 1, 1],
                               [1, 0, 1, 1], [2, 0, 1, 1], [3, 0, 1, 1], [4, 0, 1, 1], [0, 1, 1, 1],
                               [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [4, 1, 1, 1], [0, 2, 1, 1],
                               [1, 2, 1, 1], [2, 2, 1, 1], [3, 2, 1, 1], [4, 2, 1, 1], [0, 3, 1, 1],
                               [1, 3, 1, 1], [2, 3, 1, 1], [3, 3, 1, 1], [4, 3, 1, 1], [0, 0, 2, 1],
                               [1, 0, 2, 1], [2, 0, 2, 1], [3, 0, 2, 1], [4, 0, 2, 1], [0, 1, 2, 1],
                               [1, 1, 2, 1], [2, 1, 2, 1], [3, 1, 2, 1], [4, 1, 2, 1], [0, 2, 2, 1],
                               [1, 2, 2, 1], [2, 2, 2, 1], [3, 2, 2, 1], [4, 2, 2, 1], [0, 3, 2, 1],
                               [1, 3, 2, 1], [2, 3, 2, 1], [3, 3, 2, 1], [4, 3, 2, 1]]

        assert [i for i in cset] == cmp_values_inv_real  # permutes the same
        #cset.stopped = False
        for i in cset:
            print(i)

    if "set_state" in test:
        """
        Test that when a state is set it reaches the destination as if a for
        loop was used so both must give the same value
        """
        init_counters()
        # a.get_max_state() never is reached thus -1 is used here
        state = (a.get_max_state() + 15) * 3  # state to reach
        truncate = True
        if truncate:
            # cycles to reach state
            cycles = 0
            old_state = a.get_state()
            if state > old_state:
                cycles += a.get_max_state() - old_state + (state % a.get_max_state())
            else:
                cycles += state - old_state

            for i in range(cycles):
                a.increase()

            reached = a.get_state()
        else:
            if not(state < a.get_max_state() and state > 0):
                raise Exception("Non existent")
            while a.get_state() != state:
                a.increase()

            reached = a.get_state()
        a.reset()  # set counters to initial conditions
        calculated = a.set_state(state, truncate)
        # proves that counters truncates themselves
        print(
            reached,
            calculated,
            a.get_state(),
            ((state) %
             a.get_max_state()))
        assert reached == calculated == a.get_state() == ((state) % a.get_max_state())
        print("get_state tests succeded!")
    if "order" in test:
        """
        master will be the last master in the train and it is not necessarily
        the same counter so be careful. that is why MechanicalCounter was made
        so as to pack all the counters in a single object.
        """
        init_counters()
        master = a.invert_ranks()
        assert [int(i) for i in master.get_counter_train()] == [4, 3, 2, 1]
        master = master.invert_ranks()
        assert [int(i) for i in master.get_counter_train()] == [1, 2, 3, 4]
        b.invert_ranks()
        assert [int(i) for i in master.get_counter_train()] == [1, 4, 3, 2]
        master.reset()
        value = master.get_max_state()
        values_disorder = []
        for i in range(value):
            values_disorder.append(str(master.get_counter_train()))
            # print(master.get_counter_train())
            master.increase()

        cmp_values_disorder = [
            '[0, 0, 0, 0]', '[1, 0, 0, 0]', '[0, 1, 0, 0]', '[1, 1, 0, 0]',
            '[0, 2, 0, 0]', '[1, 2, 0, 0]', '[0, 3, 0, 0]', '[1, 3, 0, 0]',
            '[0, 4, 0, 0]', '[1, 4, 0, 0]', '[0, 0, 1, 0]', '[1, 0, 1, 0]',
            '[0, 1, 1, 0]', '[1, 1, 1, 0]', '[0, 2, 1, 0]', '[1, 2, 1, 0]',
            '[0, 3, 1, 0]', '[1, 3, 1, 0]', '[0, 4, 1, 0]', '[1, 4, 1, 0]',
            '[0, 0, 2, 0]', '[1, 0, 2, 0]', '[0, 1, 2, 0]', '[1, 1, 2, 0]',
            '[0, 2, 2, 0]', '[1, 2, 2, 0]', '[0, 3, 2, 0]', '[1, 3, 2, 0]',
            '[0, 4, 2, 0]', '[1, 4, 2, 0]', '[0, 0, 3, 0]', '[1, 0, 3, 0]',
            '[0, 1, 3, 0]', '[1, 1, 3, 0]', '[0, 2, 3, 0]', '[1, 2, 3, 0]',
            '[0, 3, 3, 0]', '[1, 3, 3, 0]', '[0, 4, 3, 0]', '[1, 4, 3, 0]',
            '[0, 0, 0, 1]', '[1, 0, 0, 1]', '[0, 1, 0, 1]', '[1, 1, 0, 1]',
            '[0, 2, 0, 1]', '[1, 2, 0, 1]', '[0, 3, 0, 1]', '[1, 3, 0, 1]',
            '[0, 4, 0, 1]', '[1, 4, 0, 1]', '[0, 0, 1, 1]', '[1, 0, 1, 1]',
            '[0, 1, 1, 1]', '[1, 1, 1, 1]', '[0, 2, 1, 1]', '[1, 2, 1, 1]',
            '[0, 3, 1, 1]', '[1, 3, 1, 1]', '[0, 4, 1, 1]', '[1, 4, 1, 1]',
            '[0, 0, 2, 1]', '[1, 0, 2, 1]', '[0, 1, 2, 1]', '[1, 1, 2, 1]',
            '[0, 2, 2, 1]', '[1, 2, 2, 1]', '[0, 3, 2, 1]', '[1, 3, 2, 1]',
            '[0, 4, 2, 1]', '[1, 4, 2, 1]', '[0, 0, 3, 1]', '[1, 0, 3, 1]',
            '[0, 1, 3, 1]', '[1, 1, 3, 1]', '[0, 2, 3, 1]', '[1, 2, 3, 1]',
            '[0, 3, 3, 1]', '[1, 3, 3, 1]', '[0, 4, 3, 1]', '[1, 4, 3, 1]',
            '[0, 0, 0, 2]', '[1, 0, 0, 2]', '[0, 1, 0, 2]', '[1, 1, 0, 2]',
            '[0, 2, 0, 2]', '[1, 2, 0, 2]', '[0, 3, 0, 2]', '[1, 3, 0, 2]',
            '[0, 4, 0, 2]', '[1, 4, 0, 2]', '[0, 0, 1, 2]', '[1, 0, 1, 2]',
            '[0, 1, 1, 2]', '[1, 1, 1, 2]', '[0, 2, 1, 2]', '[1, 2, 1, 2]',
            '[0, 3, 1, 2]', '[1, 3, 1, 2]', '[0, 4, 1, 2]', '[1, 4, 1, 2]',
            '[0, 0, 2, 2]', '[1, 0, 2, 2]', '[0, 1, 2, 2]', '[1, 1, 2, 2]',
            '[0, 2, 2, 2]', '[1, 2, 2, 2]', '[0, 3, 2, 2]', '[1, 3, 2, 2]',
            '[0, 4, 2, 2]', '[1, 4, 2, 2]', '[0, 0, 3, 2]', '[1, 0, 3, 2]',
            '[0, 1, 3, 2]', '[1, 1, 3, 2]', '[0, 2, 3, 2]', '[1, 2, 3, 2]',
            '[0, 3, 3, 2]', '[1, 3, 3, 2]', '[0, 4, 3, 2]', '[1, 4, 3, 2]']

        assert values_disorder == cmp_values_disorder  # tests it counts in disorder

        a.promote()
        c.demote()
        master = d.demote()
        values_disorder2 = []
        for i in range(value):
            values_disorder2.append(str(master.get_counter_train()))
            # print(master.get_counter_train())
            master.increase()

        cmp_values_disorder2 = [
            '[0, 0, 0]', '[1, 0, 0]', '[2, 0, 0]', '[0, 1, 0]', '[1, 1, 0]',
            '[2, 1, 0]', '[0, 2, 0]', '[1, 2, 0]', '[2, 2, 0]', '[0, 3, 0]',
            '[1, 3, 0]', '[2, 3, 0]', '[0, 4, 0]', '[1, 4, 0]', '[2, 4, 0]',
            '[0, 0, 1]', '[1, 0, 1]', '[2, 0, 1]', '[0, 1, 1]', '[1, 1, 1]',
            '[2, 1, 1]', '[0, 2, 1]', '[1, 2, 1]', '[2, 2, 1]', '[0, 3, 1]',
            '[1, 3, 1]', '[2, 3, 1]', '[0, 4, 1]', '[1, 4, 1]', '[2, 4, 1]',
            '[0, 0, 2]', '[1, 0, 2]', '[2, 0, 2]', '[0, 1, 2]', '[1, 1, 2]',
            '[2, 1, 2]', '[0, 2, 2]', '[1, 2, 2]', '[2, 2, 2]', '[0, 3, 2]',
            '[1, 3, 2]', '[2, 3, 2]', '[0, 4, 2]', '[1, 4, 2]', '[2, 4, 2]',
            '[0, 0, 3]', '[1, 0, 3]', '[2, 0, 3]', '[0, 1, 3]', '[1, 1, 3]',
            '[2, 1, 3]', '[0, 2, 3]', '[1, 2, 3]', '[2, 2, 3]', '[0, 3, 3]',
            '[1, 3, 3]', '[2, 3, 3]', '[0, 4, 3]', '[1, 4, 3]', '[2, 4, 3]',
            '[0, 0, 0]', '[1, 0, 0]', '[2, 0, 0]', '[0, 1, 0]', '[1, 1, 0]',
            '[2, 1, 0]', '[0, 2, 0]', '[1, 2, 0]', '[2, 2, 0]', '[0, 3, 0]',
            '[1, 3, 0]', '[2, 3, 0]', '[0, 4, 0]', '[1, 4, 0]', '[2, 4, 0]',
            '[0, 0, 1]', '[1, 0, 1]', '[2, 0, 1]', '[0, 1, 1]', '[1, 1, 1]',
            '[2, 1, 1]', '[0, 2, 1]', '[1, 2, 1]', '[2, 2, 1]', '[0, 3, 1]',
            '[1, 3, 1]', '[2, 3, 1]', '[0, 4, 1]', '[1, 4, 1]', '[2, 4, 1]',
            '[0, 0, 2]', '[1, 0, 2]', '[2, 0, 2]', '[0, 1, 2]', '[1, 1, 2]',
            '[2, 1, 2]', '[0, 2, 2]', '[1, 2, 2]', '[2, 2, 2]', '[0, 3, 2]',
            '[1, 3, 2]', '[2, 3, 2]', '[0, 4, 2]', '[1, 4, 2]', '[2, 4, 2]',
            '[0, 0, 3]', '[1, 0, 3]', '[2, 0, 3]', '[0, 1, 3]', '[1, 1, 3]',
            '[2, 1, 3]', '[0, 2, 3]', '[1, 2, 3]', '[2, 2, 3]', '[0, 3, 3]',
            '[1, 3, 3]', '[2, 3, 3]', '[0, 4, 3]', '[1, 4, 3]', '[2, 4, 3]']

        assert values_disorder2 == cmp_values_disorder2

    if "timeTest" in test:
        init_counters()
        iterations = 50000

        def test_this():
            a.get_counter_train()
            a.increase()

        # get unitary iteration time
        t1 = time.time()
        test_this()
        t2 = time.time()
        span_iter = t2 - t1  # time an iteration should last

        # get total time
        a.reset()
        t1 = time.time()
        for i in range(iterations):
            test_this()
        t2 = time.time()

        # tests time is permisible
        permisible_time = span_iter * iterations
        total_time = t2 - t1
        print(
            "Time: {}; Permissible time: {}".format(
                total_time,
                permisible_time))
        assert total_time <= permisible_time

    if "counterTest" in test:
        big_value = 10000  # iterations to leave the loop
        a.reset()

        print("Looping with evaluation")
        time_evaluation = time.time()
        limit = a.get_max_state() - 1
        a.decrease()
        for i in range(
                big_value):  # simulate while loop but with iteration limit
            a.decrease()
            if i >= limit:
                break
        print(a.get_state())
        time_evaluation = time.time() - time_evaluation

        a.reset()

        print("Looping with confirmation")
        time_confirmation = time.time()
        a.decrease_confirm()
        for i in range(
                big_value):  # simulate while loop but with iteration limit
            if a.decrease_confirm():
                break
        time_confirmation = time.time() - time_confirmation
        print(a.get_state())

        a.reset()

        print("Set the state")
        time_set = time.time()
        a.set_state(a.get_max_state() - 1, truncate=False)
        time_set = time.time() - time_set
        print(a.get_state())

        print("Time", time_evaluation, time_confirmation, time_set)
        assert time_evaluation > time_set
        assert time_confirmation > time_set
    if "Iterations" in test:
        no = 10
        digits = IntegerCounter(no)
        base = list(range(no))
        counts = []
        cmp_counts = []
        for _ in range(3):
            cmp_counts.extend(base)
            for d in digits:
                # print(d)
                counts.append(int(d))
        assert cmp_counts == counts

        init_counters()
        cset = MechanicalCounter(clist)
        cset.reset()
        base = cmp_values
        perms = []
        cmp_perms = []
        for _ in range(3):
            cmp_perms.extend(base)
            for d in cset:
                # print(d)
                perms.append(d)

        assert cmp_perms == perms
