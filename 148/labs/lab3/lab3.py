"""CSC148 Lab 3: Inheritance

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the implementation of a simple number game.
The key class design feature here is *inheritance*, which is used to enable
different types of players, both human and computer, for the game.
"""
from __future__ import annotations
import random
from typing import Tuple
from player_classes import *


################################################################################
# Below is the implementation of NumberGame.
#
# You do not have to modify this class, but you should read through it and
# understand how it uses the Player class (and its subclasses) that you'll
# be implementing.
#
# As you read through, make note of any methods or attributes a Player will
# need.
################################################################################
class NumberGame:
    """A number game for two players.

    A count starts at 0. On a player's turn, they add to the count an amount
    between a set minimum and a set maximum. The player who brings the count
    to a set goal amount is the winner.

    The game can have multiple rounds.

    === Attributes ===
    goal:
        The amount to reach in order to win the game.
    min_step:
        The minimum legal move.
    max_step:
        The maximum legal move.
    current:
        The current value of the game count.
    players:
        The two players.
    turn:
        The turn the game is on, beginning with turn 0.
        If turn is even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.

    === Representation invariants ==
    - self.turn >= 0
    - 0 <= self.current <= self.goal
    - 0 < self.min_step <= self.max_step <= self.goal
    """
    goal: int
    min_step: int
    max_step: int
    current: int
    players: Tuple[Player, Player]
    turn: int

    def __init__(self, goal: int, min_step: int, max_step: int,
                 players: Tuple[Player, Player]) -> None:
        """Initialize this NumberGame.

        Preconditions:
            0 < min_step <= max_step <= goal
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.current = 0
        self.players = players
        self.turn = 0

    def play(self) -> str:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while self.current < self.goal:
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        winner = self.whose_turn(self.turn - 1)
        return winner.name

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number.
        """
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

    def play_one_turn(self) -> None:
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.
        Print the move and the new total.
        """
        next_player = self.whose_turn(self.turn)
        amount = next_player.move(
            self.current,
            self.min_step,
            self.max_step,
            self.goal
        )
        self.current += amount

        # if current + min_step > goal, we just set a hard limit on current
        # (This is a strange corner case: don't worry about it!)
        if self.current > self.goal:
            self.current = self.goal

        self.turn += 1

        print(f'{next_player.name} moves {amount}.')
        print(f'Total is now {self.current}.')


################################################################################
# Implement your Player class and it subclasses below!
################################################################################
# TODO: Write classes Player, RandomPlayer, UserPlayer, and StrategicPlayer.
class Player:
    """
    name: simply the choice name of the player
    """
    name: str

    def __init__(self, name: str):
        self.name = name

    def move(self, current, min_step, max_step, goal) -> int:
        """
        This method is not implemented and should not be called
        perhaps you meant to create one of the subclasses of the player type
        """
        # new_score = current + amount
        # return new_score
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class RandomPlayer(Player):
    def move(self, current, min_step, max_step, goal) -> int:
        return random.randint(min_step, min(max_step, goal - current))

    def __str__(self):
        return f"{self.name}, the Random"


class UserPlayer(Player):
    def move(self, current, min_step, max_step, goal) -> int:
        amount = int(input("Amount to add to score: "))
        while amount < min_step or amount > max_step:
            print("You must add a number between the min and max amount")
            print(f"Min amount: {min_step}, Max amount: {max_step}")
            amount = int(input("Amount to add to score: "))
        return amount

    def __str__(self):
        return f"{self.name}, the User"


class StrategicPlayer(Player):
    def move(self, current, min_step, max_step, goal) -> int:
        want = goal - max_step - min_step
        if current + max_step >= goal:
            amount = max_step
        elif current + max_step >= want >= current + min_step:
            amount = want - current
            if amount + current > goal:
                return goal - current
        else:
            amount = min_step
        return amount

    def __str__(self):
        return f"{self.name}, the Robot"


def make_player(generic_name: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    name = input(f'Enter a name for {generic_name}: ')
    while True:
        type_of_player = input("Enter user for User player\nrandom for Random player\n"
                               "Or AI for Strategic player: ")
        type_of_player = type_of_player.lower()
        if type_of_player == "random":
            return RandomPlayer(name)
        elif type_of_player == "user":
            return UserPlayer(name)
        elif type_of_player == "ai":
            return StrategicPlayer(name)
        else:
            pass


def main() -> None:
    """Play multiple rounds of a NumberGame based on user input settings.
    """
    # goal = int(input('Enter goal amount: '))
    # minimum = int(input('Enter minimum move: '))
    # maximum = int(input('Enter maximum move: '))
    # p1 = make_player('p1')
    # p2 = make_player('p2')
    goal = 15
    minimum = 3
    maximum = 5
    p1 = UserPlayer("Liam")
    p2 = StrategicPlayer('Rob')
    while True:
        g = NumberGame(goal, minimum, maximum, (p1, p2))
        winner = g.play()
        print(f'And {winner} is the winner!!!')
        print(p1)
        print(p2)
        again = input('Again? (y/n) ')
        if again != 'y':
            return


if __name__ == '__main__':
    # Uncomment the following line to run the number game.
    main()

    # Uncomment the lines below to check your work using
    # python_ta and doctest.
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['random'],
    #     'allowed-io': [
    #         'main',
    #         'make_player',
    #         'move',
    #         'play_one_turn'
    #     ]
    # })
    # import doctest
    # doctest.testmod()

