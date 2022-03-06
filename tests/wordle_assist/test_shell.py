import io
import pytest
import sys

from wordle_assist.shell import WordleShell

ANSWERS = ["raise", "unfit"]

def test_reset(capsys):
    # WordleShell(answers=allowed_answers, guesses=allowed_guesses).cmdloop()
    sys.stdin = io.StringIO("guess raise 00100\nreset\nexit")
    shell = WordleShell(answers=ANSWERS, guesses=ANSWERS).cmdloop()
    out, err = capsys.readouterr()
    assert err == ""
    out_lines = out.split('\n')
    assert out_lines[0] == f'(wordle-assist) This guess reduced the set of possible solutions from {len(ANSWERS)} candidates to 1'
    assert out_lines[1] == f'(wordle-assist) Reset the set of possible solutions to {len(ANSWERS)} candidates'
