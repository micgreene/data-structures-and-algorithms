from code_challenges.insertion_sort.insertion_sort import insertion_srt as sort

import pytest

def test_insertion_sort():
    test_list = [8,4,23,42,16,15]
    actual = sort(test_list)
    expected = [4,8,15,16,23,42]

    assert actual == expected

def test_reverse_sorted():
    test_list = [20,18,12,8,5,-2]
    actual = sort(test_list)
    expected = [-2,5,8,12,18,20]

    assert actual == expected

def test_few_uniques():
    test_list = [5,12,7,5,5,7]
    actual = sort(test_list)
    expected = [5,5,5,7,7,12]

    assert actual == expected

def test_nearly_sorted():
    test_list = [2,3,5,7,13,11]
    actual = sort(test_list)
    expected = [2,3,5,7,11,13]

    assert actual == expected

def test_empty_list():
    test_list = []
    with pytest.raises(Exception):
        sort(test_list)

def test_string_list():
    test_list = [2,3,5,7,'A',1]
    with pytest.raises(Exception):
        sort(test_list)

def test_float_list():
    test_list = [2,3,5,7,2.5,1]
    with pytest.raises(Exception):
        sort(test_list)
