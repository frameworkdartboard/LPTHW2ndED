from nose.tools import *
from ex49 import lexicon, parser


def test_eat_the_bear():
    tuples = lexicon.scan("eat the bear")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
      parser.Sentence(('number', 1),
                      ('noun', 'player'), 
                      ('verb', 'eat'), 
                      ('number', 1),
                      ('noun', 'bear')))

def test_kill_the_wabbit():
    tuples = lexicon.scan("kill the wabbit")

    assert_raises(parser.ParserError, parser.parse_sentence, tuples)

def test_bear_go_north():
    tuples = lexicon.scan("bear go north")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
     parser.Sentence(('number', 1),
                     ('noun', 'bear'),
                     ('verb', 'go'),
                     ('number', 1),
                     ('direction', 'north'))) 

def test_bear_go_FNORD_north():
    tuples = lexicon.scan("bear go FNORD north")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
     parser.Sentence(('number', 1),
                     ('noun', 'bear'),
                     ('verb', 'go'),
                     ('number', 1),
                     ('direction', 'north'))) 

def test_princess_eat_the_bear():
    tuples = lexicon.scan("princess eat the bear")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
     parser.Sentence(('number', 1),
                     ('noun', 'princess'), 
                     ('verb', 'eat'), 
                     ('number', 1),
                     ('noun', 'bear'))) 
     
def test_lexluthor_stole_cakes():
    tuples = lexicon.scan("lexluthor stole cakes")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
     parser.Sentence(('number', 1),
                     ('noun', 'lexluthor'), 
                     ('verb', 'stole'), 
                     ('number', 1),
                     ('noun', 'cakes'))) 

def test_lexluthor_stole_40_cakes():
    tuples = lexicon.scan("lexluthor stole 40 cakes")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
     parser.Sentence(('number', 1),
                     ('noun', 'lexluthor'), 
                     ('verb', 'stole'), 
                     ('number', 40),
                     ('noun', 'cakes'))) 

def test_40_lexluthors_stole_1_cake():
    tuples = lexicon.scan("40 lexluthors stole 1 cake")
    parseout = parser.parse_sentence(tuples)

    assert_equals(parseout,
     parser.Sentence(('number', 40),
                     ('noun', 'lexluthors'), 
                     ('verb', 'stole'), 
                     ('number', 1),
                     ('noun', 'cake'))) 

