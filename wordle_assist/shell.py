import cmd
from copy import deepcopy

from wordle_assist.wordle import process_guess, suggest_guess

class WordleShell(cmd.Cmd):
    intro = 'Welcome to a wordle assistant.   Type help or ? to list commands.\n'
    prompt = '(wordle-assist) '

    def __init__(self, answers, guesses):
        super(WordleShell, self).__init__()
        self.initial_answers = deepcopy(answers)
        self.answers = answers
        self.guesses = guesses

    def do_show(self, arg):
        'Show all remaining possible words.'
        print(self.answers)

    def do_suggest(self, arg):
        'Suggest a number of words to guess. ex: SUGGEST 10'
        num_suggestions = 1
        if len(arg) > 0:
            num_suggestions = max(num_suggestions, int(arg))
        print(suggest_guess(guesses=self.guesses, answers=self.answers, num_suggestions=num_suggestions))

    def do_reset(self, arg):
        'Resets the current set of possible words to the full set (undoes all guesses).  ex: RESET'
        self.answers = deepcopy(self.initial_answers)

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
        old_num_answers = len(self.answers)
        self.answers = process_guess(self.answers, word, result)
        print(f'This guess reduced the set of possible solutions from {old_num_answers} candidates to {len(self.answers)}')
    
    def do_exit(self, arg):
        'Exit the wordle assistant'
        return True