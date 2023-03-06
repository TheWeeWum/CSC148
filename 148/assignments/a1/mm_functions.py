"""CSC108/CSCA08: Fall 2022 -- Assignment 1: Mystery Message Game

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane
Horton, Michael Liut, Jacqueline Smith, Anya Tafliovich and Michelle Craig.
"""

from constants import (CONSONANT_POINTS, VOWEL_COST, CONSONANT_BONUS,
                       PLAYER_ONE, PLAYER_TWO, CONSONANT, VOWEL,
                       SOLVE, QUIT, HUMAN, HUMAN_HUMAN,
                       HUMAN_COMPUTER, EASY, HARD, ALL_CONSONANTS,
                       ALL_VOWELS, PRIORITY_CONSONANTS, HIDDEN)


# We provide this function as an example.
def is_win(view: str, message: str):
    return message == view


# We provide this function as an example of using a function as a helper.
def is_game_over(view: str, message: str, move: str):
    return move == QUIT or is_win(view, message)


# We provide the header and docstring of this function as an example
# of where and how to use constants in the docstring.
def is_human(current_player: str, game_type: str):
    if game_type == HUMAN_COMPUTER and current_player == PLAYER_TWO:
        return False
    else:
        return True


def is_one_player_game(current_player):
    # or perhaps current_player == "human"
    return current_player == PLAYER_ONE


def current_player_score(score1, score2, current_player):
    if current_player == PLAYER_ONE:
        return score1
    else:
        return score2


def is_bonus_letter(cur_view, letter, message):
    if letter in message and letter not in cur_view:
        return True
    else:
        return False


def get_updated_char_view(cur_view, message, index, guess):
    if message[index] == guess:
        return guess
    else:
        return cur_view[index]


def calculate_score(cur_score, occurences, cur_move):
    if cur_move == VOWEL:
        return cur_score - 1
    else:
        return cur_score + occurences


def next_player(cur_player, occurences, game_type):
    if game_type == HUMAN or occurences != 0:
        return PLAYER_ONE
    else:  # unecessary but better for understandability
        if cur_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE


def is_fully_hidden(cur_view, index, message):
    if message[index] in cur_view:
        return False
    else:
        return True


def computer_chooses_solve(cur_view, difficulty, consonants):
    if consonants == []:  # same as if not consonants
        return True

    elif difficulty == HARD:
        return cur_view.count("^") > len(cur_view) / 2
    
    else:
        return False


def erase(string, index):

    if 0 <= index < len(string):
        return string[:index] + string[index + 1:]
    else:
        return string


# Helper function for computer_chooses_solve
# This function is already complete. You must not modify it.
def half_revealed(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False
    """

    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic += 1
    return num_alphabetic >= num_hidden
