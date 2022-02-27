# wordle-assist
A simple tool to assist wordle players



# Instructions
## Setup
To create the `wordle-assist` environment:
```
conda env create -f environment.yml
``` 
which should install all requirements,
then to activate it:
```
conda activate wordle-assist
```

## Usage
Run the tool with:
```
python wordle-assist.py
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


