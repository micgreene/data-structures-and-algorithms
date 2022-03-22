from code_challenges.hashmap_left_join.hashmap_left_join import left_join
from code_challenges.hashmap_left_join.hash_table import Hashtable

import pytest

def test_left_join():
    syn_table = Hashtable()

    ant_table = Hashtable()

    syn_table.set('diligent', 'employed')
    syn_table.set('fond', 'enamored')
    syn_table.set('guide' 'usher')
    syn_table.set('outfit', 'garb')
    syn_table.set('wrath' 'anger')

    ant_table.set('diligent', 'idle')
    ant_table.set('fond', 'averse')
    ant_table.set('guide', 'follow')
    ant_table.set('flow', 'jam')
    ant_table.set('wrath', 'delight')

    actual = left_join(syn_table, ant_table)
    expected = [
        ["font", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["guide", "usher","follow"]
    ]

    assert actual == expected
