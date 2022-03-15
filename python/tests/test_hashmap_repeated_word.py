from code_challenges.hashmap_repeated_word.hashmap_repeated_word import repeated_word, no_punc

import pytest

def test_repeated_word_article():
    test_str = 'Once upon a time, there was a brave princess who...'

    actual = repeated_word(test_str)
    expected = 'a'

    assert actual == expected

def test_repeated_word_preposition():
    test_str = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'

    actual = repeated_word(test_str)
    expected = 'it'

    assert actual == expected

def test_repeated_word_noun():
    test_str = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'

    actual = repeated_word(test_str)
    expected = 'summer'

    assert actual == expected

def test_repeated_word_num():
    test_str = 'Wow1, a cool wow1.'

    actual = repeated_word(test_str)
    expected = 'wow1'

    assert actual == expected

def test_repeated_word_not_found():
    test_str = 'There is only one instance of each word in this sentence.'

    with pytest.raises(Exception):
        repeated_word(test_str)

def test_no_punc():
    test_str = 'there!@#$%^'

    actual = no_punc(test_str)
    expected = 'there'

    assert actual == expected

def test_no_punc_capital():
    test_str = 'THERE'

    actual = no_punc(test_str)
    expected = 'there'

    assert actual == expected

def test_no_punc_only_punc():
    test_str = '!@#$%^&*()-+'

    actual = no_punc(test_str)
    expected = ''

    assert actual == expected

def test_no_punc_empty():
    test_str = ''

    actual = no_punc(test_str)
    expected = ''

    assert actual == expected
