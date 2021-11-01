import sys
import pytest
sys.path.append('..')
from twitter  import get_latest_thirty_tweets as gt

# regular implementation
def test_normal():
    handle = "POTUS"
    assert gt(handle) != pytest.raises(ValueError)

# handles with letters
def test_alphanumeric():
    handle = "POTUS1"
    assert gt(handle) != pytest.raises(ValueError)

# handles only digits
def test_digits():
    handle = "78687"
    assert gt(handle) != pytest.raises(ValueError)

# handles can have underscore
def test_underscore():
    handle = "_fahadfarid"
    assert gt(handle) != pytest.raises(ValueError) 

# handles can not have other symbol
def test_symbol():
    handle = "?fahadfarid"
    assert gt(handle) == pytest.raises(ValueError) 

# handles can not be longer than 15 character
def test_length():
    handle = "_djkbchsknkcbshnladkjnskjenmsjkdcn"
    assert gt(handle) == pytest.raises(ValueError)     

# checks if input sanitization is done (cybersecurity issue)
def test_input_sanitization():
    handle = "hahsg'print(keys)"
    assert gt(handle) == pytest.raises(TypeError)
