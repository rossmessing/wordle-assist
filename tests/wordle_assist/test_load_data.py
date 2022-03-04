import os
from tempfile import TemporaryDirectory

from wordle_assist.constants import ALLOWED_ANSWERS_URL, ALLOWED_GUESSES_URL
from wordle_assist.load_data import load_word_lists, read_word_list_file

WORD_LIST = ['abc', 'def']

def test_read_word_list_file():
    with TemporaryDirectory() as d:
        temp_file_name = os.path.join(d, 'temp_word_list.txt')
        fh = open(temp_file_name, "w")
        for word in WORD_LIST:
            fh.write(word+"\n")
        fh.close()
        read_list = read_word_list_file(temp_file_name)
    assert len(read_list) == len(WORD_LIST)
    assert all([a == b for a, b in zip(read_list, WORD_LIST)])

# test that we can download the word lists, and that their sizes are appropriate
def test_load_word_lists():
    with TemporaryDirectory() as d:
        answers, guesses = load_word_lists(
            allowed_answers_url=ALLOWED_ANSWERS_URL,
            allowed_answers_filename=os.path.join(d, "answers.txt"),
            allowed_guesses_url=ALLOWED_GUESSES_URL,
            allowed_guesses_filename=os.path.join(d, "answers.txt")
        )
        assert 3000 > len(answers) > 1000
        assert 20000 > len(guesses) > 10000
