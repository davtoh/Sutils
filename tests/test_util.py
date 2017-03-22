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
from sutils import copy_support, BaseCopySupporter

# @copy_support is equivalent of inheriting from BaseCopySupporter
# _convert.update({'__call__':_convert["spawn"]})
@copy_support
class CopySupporterTest(object):
    def __init__(self, name, flag = False):
        self.name = name
        self.flag = flag


@copy_support(_map = {"to_map":"mapped"})
class CopySupporterTest2(object):
    def __init__(self, name, flag = False, to_map = None):
        self.name = name
        self.flag = flag
        self.mapped = to_map


@copy_support(_map = {"name":"child_name", "not_in_self":None})
class CopyInheritanceTest(CopySupporterTest):# inheritance
    def __init__(self, name, in_self = None, not_in_self = None):
        # here data parameter is supposed to be defined in parent class
        self.child_name = name
        self.in_self = in_self # well behaved variable
        # not_in_self is not assigned to any variable
        super(CopyInheritanceTest, self).__init__("Parent name")

if __name__ == "__main__":

    additional = "Other variable"
    # Test spawn and clone from Carriers
    A = CopySupporterTest("Original", flag = True)
    A.additional = additional

    B = A.spawn()
    C = A.clone()
    # print(repr(A))
    assert repr(A) == "CopySupporterTest(name = 'Original', flag = True)"
    # print(repr(B))
    assert repr(B) == repr(A)
    assert hasattr(B,"additional") == False
    # print(repr(C))
    assert repr(C) == repr(A)
    assert C.additional == additional

    B = A("Spawned and modified", flag = False)  # equivalent to call A.spawn
    C = A.clone("Cloned and modified", flag = False)
    # print(repr(B))
    assert repr(B) == "CopySupporterTest(name = 'Spawned and modified', flag = False)"
    assert hasattr(B,"additional") == False
    # print(repr(C))
    assert repr(C) == "CopySupporterTest(name = 'Cloned and modified', flag = False)"
    assert C.additional == additional


    # Test @copy_support with parameters and mapping
    A2 = CopySupporterTest2("Original 2")
    A2.additional = additional

    B2 = A2("Spawned 2")  # equivalent to call A.spawn
    C2 = A2.clone("Cloned 2")
    # print(repr(A2))
    assert repr(A2) == "CopySupporterTest2(name = 'Original 2', flag = False, to_map = None)"
    # print(repr(B2))
    assert repr(B2) == "CopySupporterTest2(name = 'Spawned 2', flag = False, to_map = None)"
    assert hasattr(B2,"additional") == False
    # print(repr(C2))
    assert repr(C2) == "CopySupporterTest2(name = 'Cloned 2', flag = False, to_map = None)"
    assert C2.additional == additional

    B2 = A2(name = "Spawned 2 and modified", to_map = "Mapped variable")  # equivalent to call A.spawn
    C2 = A2.clone(name = "Cloned 2 and modified", to_map = "Mapped variable")
    # print(repr(B2))
    assert repr(B2) == "CopySupporterTest2(name = 'Spawned 2 and modified', flag = False, to_map = 'Mapped variable')"
    assert hasattr(B2,"additional") == False
    # print(repr(C2))
    assert repr(C2) == "CopySupporterTest2(name = 'Cloned 2 and modified', flag = False, to_map = 'Mapped variable')"
    assert C2.additional == additional

    # Test spawn and clone from Inheritors
    A3 = CopyInheritanceTest("Original inheritor")
    A3.additional = additional

    B3 = A3("Spawned inheritor")  # equivalent to call A.spawn
    C3 = A3.clone("Cloned inheritor")
    #print(repr(A3))
    assert repr(A3) == "CopyInheritanceTest(name = 'Original inheritor', in_self = None)"
    #print(repr(B3))
    assert repr(B3) == "CopyInheritanceTest(name = 'Spawned inheritor', in_self = None)"
    assert hasattr(B3,"additional") == False
    #print(repr(C3))
    assert repr(C3) == "CopyInheritanceTest(name = 'Cloned inheritor', in_self = None)"
    assert C3.additional == additional