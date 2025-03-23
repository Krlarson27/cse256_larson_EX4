import pytest
from guess_the_word import chose_word, display_word

word = ["python", "computer", "science", "programming", "github"]

def test_chose_word():
    word = chose_word()
    assert word in word

def test_display_word():
    word = "python"
    guessed_letters = {"p", "o"}
    assert display_word(word, guessed_letters) == "p___o_"
