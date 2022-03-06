import io
import pytest
import sys

from wordle_assist.shell import INTRO, PROMPT, WordleShell

ANSWERS = ["raise", "unfit"]

def command_string(commands):
    return "\n".join(commands + ["exit"])


def test_reset(capsys):
    commands = ["guess raise 00100", "reset"]
    sys.stdin = io.StringIO(command_string(commands))
    WordleShell(answers=ANSWERS, guesses=ANSWERS).cmdloop()
    out, err = capsys.readouterr()
    assert err == ""
    out_lines = out.split('\n')
    assert out_lines[0] == INTRO
    assert out_lines[1] == f'{PROMPT}This guess reduced the set of possible solutions from {len(ANSWERS)} candidates to 1'
    assert out_lines[2] == f'{PROMPT}Reset the set of possible solutions to {len(ANSWERS)} candidates'
