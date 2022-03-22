from code_challenges.hashmap_left_join.hashmap_left_join import left_join
from code_challenges.hashmap_left_join.hash_table import Hashtable

import pytest

def test_left_join():
    syn_table = Hashtable()

    ant_table = Hashtable()

    syn_table.set('diligent', 'employed')
    syn_table.set('fond', 'enamored')
    syn_table.set('guide', 'usher')
    syn_table.set('outfit', 'garb')
    syn_table.set('wrath', 'anger')

    ant_table.set('diligent', 'idle')
    ant_table.set('fond', 'averse')
    ant_table.set('guide', 'follow')
    ant_table.set('flow', 'jam')
    ant_table.set('wrath', 'delight')

    actual = left_join(syn_table, ant_table)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['outfit', 'garb', None],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', 'follow']
    ]

    assert actual == expected

def test_no_matches():
    syn_table = Hashtable()

    ant_table = Hashtable()

    syn_table.set('diligent', 'employed')
    syn_table.set('fond', 'enamored')
    syn_table.set('guide', 'usher')
    syn_table.set('outfit', 'garb')
    syn_table.set('wrath', 'anger')

    ant_table.set('dig', 'bury')
    ant_table.set('run', 'walk')
    ant_table.set('cheerful', 'grumpy')
    ant_table.set('burn', 'extinguish')
    ant_table.set('yell', 'whisper')

    actual = left_join(syn_table, ant_table)
    expected = [
        ['fond', 'enamored', None],
        ['wrath', 'anger', None],
        ['outfit', 'garb', None],
        ['diligent', 'employed', None],
        ['guide', 'usher', None]
    ]

    assert actual == expected

def test_int_in_table():
    syn_table = Hashtable()

    ant_table = Hashtable()

    syn_table.set('diligent', 'employed')
    syn_table.set('fond', 'enamored')
    syn_table.set('guide', 'usher')
    syn_table.set('outfit', 'garb')
    syn_table.set('wrath', 'anger')

    ant_table.set('diligent', 'idle')
    ant_table.set('fond', 'averse')
    ant_table.set('guide', 'follow')
    ant_table.set('many', 1)
    ant_table.set('wrath', 'delight')

    with pytest.raises(Exception):
        actual = left_join(syn_table, ant_table)
