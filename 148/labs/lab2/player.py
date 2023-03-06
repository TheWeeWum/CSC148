"""Object-Oriented Programming: Twitter example

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains the player class for lab2.
"""


class Player:
    """ A player in an arbitrary video game

    === Attributes ===
    player: the name of the player
    scores: scores achieved by the player in all their games played

    === Sample Usage ===
    >>> p1 = Player("Ian", [10.5])
    >>> p1.add_score(5.7)
    >>> p1.add_score(2.5)
    >>> p1.add_score(21.3)
    >>> p1.add_score(6.6)
    >>> p1.average(3)
    10.133333333333333
    >>> p1.player
    'Ian'
    >>> p1.scores
    [10.5, 5.7, 2.5, 21.3, 6.6]
    """
    # Attribute Types
    player: str
    scores: list[float]

    def __init__(self, name: str, scores: list[float] = []):
        self.player = name
        self.scores = scores

    def add_score(self, score: float):
        self.scores.append(score)
        if len(self.scores) == 101:
            self.scores.pop(0)

    def average(self, num: int):
        total = 0
        if num > len(self.scores):
            return -1
        for score in self.scores[-num:]:
            total += score
        return total / num

    def clear_scores(self):
        self.scores = []

    def low_score(self):
        low = self.scores[0]
        for score in self.scores:
            if score < low:
                low = score
        return low

    def top_score(self):
        best = 0
        for score in self.scores:
            if score > best:
                best = score
        return best
