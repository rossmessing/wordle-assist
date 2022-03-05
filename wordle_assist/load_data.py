from os.path import exists
from urllib.request import urlretrieve


from wordle_assist.constants import (
    ALLOWED_ANSWERS_URL, 
    ALLOWED_ANSWERS_FILENAME,
    ALLOWED_GUESSES_URL, 
    ALLOWED_GUESSES_FILENAME)


def read_word_list_file(filename):
    """
    Reads a text word list into a list of words, each of which have length word_length
    """
    with open(filename, 'r') as fh:
        return [line.strip() for line in fh]


def load_word_lists(
    allowed_answers_url=ALLOWED_ANSWERS_URL,
    allowed_answers_filename=ALLOWED_ANSWERS_FILENAME,
    allowed_guesses_url=ALLOWED_GUESSES_URL,
    allowed_guesses_filename=ALLOWED_GUESSES_FILENAME):
    """
    Returns the word lists of allowed guesses and allowed answers
    If word lists aren't present, download them.
    """
    if not exists(ALLOWED_ANSWERS_FILENAME):
        urlretrieve(ALLOWED_ANSWERS_URL, filename=ALLOWED_ANSWERS_FILENAME)
    if not exists(ALLOWED_GUESSES_FILENAME):
        urlretrieve(ALLOWED_GUESSES_URL, filename=ALLOWED_GUESSES_FILENAME)
    return read_word_list_file(ALLOWED_ANSWERS_FILENAME), read_word_list_file(ALLOWED_GUESSES_FILENAME)