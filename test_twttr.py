import pytest
from twttr import shorten

def test_shorten_one_word():
    assert shorten('Twitter') == 'Twttr'

def test_shorten_no_word():
    assert shorten('') == ''

def test_upper_cases():
    assert shorten('TEfloWeA') == 'TflW'
