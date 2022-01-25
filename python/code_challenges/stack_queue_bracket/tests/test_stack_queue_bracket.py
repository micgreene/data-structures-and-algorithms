from ..stack_queue_bracket import validate_brackets
import pytest

# test1 = '{}(){}'
# test2 = '()[[Extra Characters]]'
# test3 = '{}{Code}[Fellows](())'
# test4 = '[({}]'
# test5 = '(]('
# test6 = '{(})'
# test7 = '{'
# test8 = ')'
# test9 = '[}'

def test_one():
    test1 = '{}(){}'

    actual = validate_brackets(test1)
    expected = True
    assert actual == expected

def test_two():
    test2 = '()[[Extra Characters]]'

    actual = validate_brackets(test2)
    expected = True
    assert actual == expected

def test_three():
    test3 = '{}{Code}[Fellows](())'

    actual = validate_brackets(test3)
    expected = True
    assert actual == expected

def test_four():
    test4 = '[({}]'

    actual = validate_brackets(test4)
    expected = False
    assert actual == expected

def test_five():
    test5 = '(]('

    actual = validate_brackets(test5)
    expected = False
    assert actual == expected

def test_six():
    test6 = '{(})'

    actual = validate_brackets(test6)
    expected = False
    assert actual == expected

def test_seven():
    test7 = '{'

    actual = validate_brackets(test7)
    expected = False
    assert actual == expected

def test_eight():
    test8 = ')'

    actual = validate_brackets(test8)
    expected = False
    assert actual == expected

def test_nine():
    test9 = '[}'

    actual = validate_brackets(test9)
    expected = False
    assert actual == expected
