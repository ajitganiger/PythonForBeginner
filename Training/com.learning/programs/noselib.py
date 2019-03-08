from numpy.core.defchararray import multiply

__author__ = 'aganiger'


def test_numbers_3_4():
    assert 3*4 == 12


def test_strings_a_3():
    assert multiply('a', 3) == 'aaa'