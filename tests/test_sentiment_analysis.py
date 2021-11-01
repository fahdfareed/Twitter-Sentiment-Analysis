import sys
sys.path.append('..')
from twitter  import sentiment_analysis as sa

# test if everything is ok
def test_normal():
    argument = ['bad']
    assert sa(argument) == ['Negative']

# test if it crashes on numerical
def test_stress():
    long_argument = ['bad'] * 100
    assert sa(long_argument) == (['Negative'] * 100)

# check if it returns positive, negative and neural and not just single value
def test_correctly():
    argument = ['good', 'normal', 'bad']
    assert sa(argument) == ['Positive', 'Neutral', 'Negative']

# test small number
def test_numbers():
    argument = ['8', '605', '387']
    assert sa(argument) == ['Neutral'] * 3

# test large number
def test_large_numbers():
    argument = ['654549785669827658', '654464654605', '38654565466545466546547']
    assert sa(argument) == ['Neutral'] * 3

# test non words
def test_non_words():
    argument = ['3vil', 'l33t0rs', 'd3c1d3d', '4our', 'n0T', 'd3sign3ers', 'wefkbhjweb', 'bwdccwdbjbhj', 'uwtfqytfw']
    assert sa(argument) == ['Neutral'] * 9
