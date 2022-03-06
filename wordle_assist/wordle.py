def process_guess(word_list, guess, result):
    """
    Takes in the current list of possible words, a guess string, and a result string
    Returns the new list of possible words
    """
    assert len(guess) == 5, f"Word ({guess}) must have length 5"
    assert len(guess) == len(result), f'Result ({result}) must have the same length as word ({word})'
    for r in result:
        assert r in {'0', '1', '2'}, "Result characters must be 0, 1 or 2"
    to_remove = set()
    wrong_pos = set()
    right_pos = set()
    for position, (letter, result) in enumerate(zip(guess, result)):
        if result == '0':  # letter not in word at all
            to_remove.add(letter)
        elif result == '1':  # wrong position
            wrong_pos.add((letter, position))
        else:  # right position
            right_pos.add((letter, position))
    
    new_word_list = []
    for word in word_list:
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
    return new_word_list


def generate_result(guess, solution):
    """ returns result string for guess if solution is the word being guessed"""
    unmatched_chars = set()
    return_string_array = [0, 0, 0, 0, 0]
    for i, (g, s) in enumerate(zip(guess, solution)):
        if g == s:
            return_string_array[i] = 2
        else:
            unmatched_chars.add(s)
    for i, (g, s) in enumerate(zip(guess, solution)):
        if g != s and g in unmatched_chars:
            return_string_array[i] = 1
    return ''.join([str(i) for i in return_string_array])


def suggest_guess(guesses, answers, num_suggestions=1):
    """
    Suggests guesses that minimize the number of possible solutions remaining
    """
    guess_sum = {}
    for guess in guesses + answers:
        guess_sum[guess] = 0
        for solution in answers:
            guess_sum[guess] += len(process_guess(answers, guess, generate_result(guess, solution)))
    ordered_guesses = [k for k in sorted(guess_sum, key=guess_sum.get)]
    return ordered_guesses[:num_suggestions]