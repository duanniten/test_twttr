import pytest
from twttr import shorten

def test_shorten_one_word():
    assert shorten('Twitter') == 'Twttr'

def test_shorten_no_word():
    assert shorten('') == ''

def test_shorten_int():
    assert shorten(1) == '1'