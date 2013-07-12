from nose.tools import *
from ex49 import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east west")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east'),
                          ('direction', 'west')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in a of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'a'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess dumbbell")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess'),
                          ('noun', 'dumbbell')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234 0 -1234")
    assert_equal(result, [('number', 3),
                          ('number', 91234),
                          ('number', 0),
                          ('number', -1234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])

def test_variety():
    result = lexicon.scan("909 URF of 9 eat dumbbell bear")
    assert_equal(result, [('number', 909),
                          ('error', 'URF'),
                          ('stop', 'of'),
                          ('number', 9),
                          ('verb', 'eat'),
                          ('noun', 'dumbbell'),
                          ('noun', 'bear')])

def test_case_insensitivity():
    result = lexicon.scan("909 OOPSALA A bEAR kill GO")
    assert_equal(result, [('number', 909),
                          ('error', 'OOPSALA'),
                          ('stop', 'a'),
                          ('noun', 'bear'),
                          ('verb', 'kill'),
                          ('verb', 'go')])
