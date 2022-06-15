import pytest


def test_simple_word():
    max_len = 15
    phrase = input("Set a phrase: ")
    assert len(phrase) < max_len, f"Phrase longer than {max_len}"