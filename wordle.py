from wordle.load_data import load_word_lists
from wordle.shell import WordleShell


if __name__ == '__main__':
    allowed_guesses, allowed_answers = load_word_lists()
    WordleShell(guesses=allowed_guesses, answers=allowed_answers).cmdloop()