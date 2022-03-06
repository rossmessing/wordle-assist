# wordle-assist
A simple tool to assist [wordle](https://www.nytimes.com/games/wordle/index.html) players.

This tool suggests words to guess, 
and tracks the set of possible words given guesses and results so far.

The tool models the state of wordle as the set of possible words that may be the puzzle solution.
Each guess eliminates possible words.

For suggestion, this tool uses a simple $n^3$ algorithm.
* For each possible guess
  * For each possilbe solution
    * How many words does this guess remove from the set of possible solutions?


# Instructions
## Conda Setup
To create the `wordle_assist` environment:
```
conda env create -f environment.yml
``` 
which should install all requirements,
then to activate it:
```
conda activate wordle_assist
```

## Usage
Run the tool with:
```
python wordle_assist.py
```

This takes you to an interactive experience with a few commands:
* `help`: This will list all commands
* `exit`: This will exit the tool
* `show`: This will show all the words that are still possible solutions
* `guess word result`: this will process a wordle guess and result, 
removing all solutions that are rendered invalid by the guess.
Sample usage: `guess unfit 00102` would correspond to guessing 
the word `unfit` and receiving as a result:
  * the letters `u` and `n` in grey
  * `f` in yellow (right letter, wrong place)
  * the letter `i` in grey
  * the letter `t` in green (right letter, right place)
* `suggest n`: This suggests n words to guess.
* `reset`: Resets the set of possible words to the full initial set (undoes guesses)

## Development
To develop this package, you'll generally want to install this package with 
```
pip install -e .
```
and validate that that worked correctly by running tests
```
python -m pytest
```

## Docker Workflow
To build the container, run 
```
docker build -t wordle_assist .
```

To execute the container, run:
```
docker run -it wordle_assist
```