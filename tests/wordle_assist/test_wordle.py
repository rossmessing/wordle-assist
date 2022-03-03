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