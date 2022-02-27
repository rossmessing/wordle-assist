import cmd
import os

import wget

# this wordlist is the list of all possible solutions, as derived from the original game's javascript source
WORD_LIST_URL = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/5d752e5f0702da315298a6bb5a771586d6ff445c/wordle-answers-alphabetical.txt"
WORD_LIST_FILENAME="words.txt"
WORD_LENGTH = 5

def load_dictionary(url=WORD_LIST_URL, filename=WORD_LIST_FILENAME, word_length=WORD_LENGTH):
    """
    Returns a list of words of length word_length from the words in filename.  If filename isn't present, downloads it.
    """
    if not os.path.exists(WORD_LIST_FILENAME):
        wget.download(WORD_LIST_URL, WORD_LIST_FILENAME)
    with open(WORD_LIST_FILENAME, 'r') as fh:
        return [line.strip() for line in fh if len(line.strip()) == WORD_LENGTH]


class WordleShell(cmd.Cmd):
    intro = 'Welcome to a wordle assistant.   Type help or ? to list commands.\n'
    prompt = '(wordle-assist) '

    def __init__(self, word_list):
        super(WordleShell, self).__init__()
        self.word_list = word_list

    def do_show(self, arg):
        'Show all remaining possible words.'
        print(self.word_list)

    def do_guess(self, arg):
        '''
        Process a guess and result: 
        0 for no match (grey)
        1 for right letter in the wrong place (yellow)
        2 for right letter in the right place (green)
        ex: GUESS unfit 00222
        '''
        arg_split = arg.split()
        word = arg_split[0].strip()
        result = arg_split[1].strip()
        assert len(word) == WORD_LENGTH, f"Word ({word}) must have length {WORD_LENGTH}"
        assert len(word) == len(result), f'Result ({result}) must have the same length as word ({word})'
        for r in result:
            assert r in {'0', '1', '2'}, "Result characters must be 0, 1 or 2"
        to_remove = set()
        wrong_pos = set()
        right_pos = set()
        for position, (letter, result) in enumerate(zip(word, result)):
            if result == '0':  # letter not in word at all
                to_remove.add(letter)
            elif result == '1':  # wrong position
                wrong_pos.add((letter, position))
            else:  # right position
                right_pos.add((letter, position))
        old_word_list_size = len(self.word_list)
        new_word_list = []
        for word in self.word_list:
            retain = True
            # first check if it's got a letter to be removed
            for c in to_remove:
                if c in word:
                    retain = False
                    break
            if not retain:
                continue
            # now check if it's got a letter in the right place
            for l, i in right_pos:
                if word[i] != l:
                    retain = False
                    break
            if not retain:
                continue
            # now check if it DOESN'T have a letter in the wrong place, but DOES have that letter
            for l, i in wrong_pos:
                if (word[i] == l) or (l not in word):
                    retain = False
                    break
            if not retain:
                continue
            new_word_list.append(word)
        self.word_list = new_word_list
        print(f'This guess reduced the set of possible solutions from {old_word_list_size} candidates to {len(self.word_list)}')
    
    def do_exit(self, arg):
        'Exit the wordle assistant'
        return True


if __name__ == '__main__':
    WordleShell(word_list=load_dictionary()).cmdloop()