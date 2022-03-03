import os
from tempfile import TemporaryDirectory

from wordle_assist.load_data import read_word_list_file

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

