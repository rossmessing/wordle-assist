from wordle_assist.load_data import load_word_lists
from wordle_assist.shell import WordleShell


if __name__ == '__main__':
    allowed_answers, allowed_guesses = load_word_lists()
    WordleShell(answers=allowed_answers, guesses=allowed_guesses).cmdloop()