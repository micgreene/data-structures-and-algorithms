from code_challenges.hash_table.hash_table import Hashtable

import pytest

def test_hash_table():
    ht = Hashtable()
    ht.set('apple', 8)
    expected = True
    actual = ht.contains('apple') == True
    assert actual == expected

def test_get_key():
    ht = Hashtable()
    ht.set('apple', 8)
    expected = 8
    actual = ht.get('apple')
    assert actual == expected

def test_not_in_table():
    ht = Hashtable()
    ht.set('apple', 8)
    expected = None
    actual = ht.get('orange')
    assert actual == expected

def test_keys():
    ht = Hashtable()
    ht.set('apple', 8)
    ht.set('orange', 7)
    ht.set('pear', 6)
    ht.set('grape', 9)
    ht.set('peach', 2)
    actual = ht.keys()
    expected = ['pear', 'apple', 'orange', 'peach', 'grape']
    assert actual == expected

def test_collision():
    ht = Hashtable()
    ht.set('appel', 8)
    ht.set('aplpe', 9)

    actual = ht.contains('appel')
    expected = True
    assert actual == expected

    actual = ht.contains('aplpe')
    expected = True
    assert actual == expected

def test_value_collision():
    ht = Hashtable()
    ht.set('appel', 8)
    ht.set('aplpe', 9)
    ht.set('paple', 10)

    actual = ht.get('appel')
    expected = 8
    assert actual == expected

    actual = ht.get('aplpe')
    expected = 9
    assert actual == expected

    actual = ht.get('paple')
    expected = 10
    assert actual == expected

def test_hash_table():
    ht = Hashtable()
    ht.set('apple', 8)
    expected = True
    actual = ht.contains('apple') == True
    assert actual == expected
