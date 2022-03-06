import pytest

from wordle_assist.wordle import generate_result

#def process_guess(word_list, guess, result):

#def generate_result(guess, solution)

#def suggest_guess(guesses, answers, num_suggestions=1)

WORD = "hyper"
NON_OVERLAPPING_WORD = "unfit"

def test_generate_result_solution():
    assert "22222" == generate_result(WORD, WORD)


def test_generate_result_non_overlapping():
    assert "00000" == generate_result(WORD, NON_OVERLAPPING_WORD)

def test_generate_result_partial_overlap():
    test_word = WORD[:3] + NON_OVERLAPPING_WORD[3:]
    assert "22200" == generate_result(test_word, WORD)

def test_handles_double_letters():
    three = "lolly"
    two = "pully"
    assert "00222" == generate_result(two, three)
    assert "00222" == generate_result(three, two)