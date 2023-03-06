"""Prep 2 Synthesize Sample Tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu, Diane Horton, and Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 David Liu, Diane Horton, and Sophia Huynh

=== Module Description ===
This module contains sample tests for Prep 2.
Complete the TODO in this file.
There is also a task inside prep2.py.
Make sure to look at that file and complete the TODO there as well.

We suggest you also add your own tests to practice writing tests and
to be confident your code is correct.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here

All test cases must have different names (i.e. you cannot have two tests
named test_my_test_case).
"""
from hypothesis import given
from hypothesis.strategies import integers
from prep2 import Spinner, Tweet
from datetime import date


################################################################################
# Part 3
# In this part, you will be fixing a bug within a provided test.
################################################################################
def test_buggy_consecutive_spins() -> None:
    """Test consecutive spins of your Spinner class.
    This test case has a bug in it."""

    s = Spinner(6)                          # Do not change this line
    s.spin(2)                               # Do not change this line
    expected_value1 = 2
    assert s.position == expected_value1    # Do not change this line
    s.spin(2)                               # Do not change this line
    expected_value2 = 4
    assert s.position == expected_value2    # Do not change this line


################################################################################
# Sample test cases below
#
# Use the below test cases as an example for writing your own test cases,
# and as a start to testing your prep2.py code.
#
# The self-test on MarkUs runs the tests below, along with a few others.
# Make sure you run the self-test after submitting your code!
#
# WARNING: THIS IS CURRENTLY AN EXTREMELY INCOMPLETE SET OF TESTS!
# We will test your code on a much more thorough set of tests!
################################################################################
def test_doctest() -> None:
    """Test the given doctest in the Spinner class docstring."""
    spinner = Spinner(8)

    spinner.spin(4)
    assert spinner.position == 4

    spinner.spin(2)
    assert spinner.position == 6

    spinner.spin(2)
    assert spinner.position == 0


def test_extreme_force() -> None:
    """
    Test the spinner class when the number
    of spins is more than a full rotation
    """
    spinner = Spinner(10)
    spinner.spin(10)
    assert spinner.position == 0
    spinner.spin(101)
    assert spinner.position == 1
    spinner.spin(8)
    assert spinner.position == 9
    spinner.spin(3)
    assert spinner.position == 2


def test_tornado() -> None:
    """
    Goes through all possible positions on the spinner
    adding one each time
    Simply here for bulk test in order to make sure each slot
    on the spinner works
    """
    counter = 0
    spinner = Spinner(10)
    actual = 0
    while counter < 30:
        counter += 1
        spinner.spin(1)
        actual += 1
        if actual == 10:
            actual = 0
        assert spinner.position == actual


def test_zero_force() -> None:
    """
    Tests the ability to spin it 0 positions
    """
    spinner = Spinner(10)
    spinner.spin(0)
    assert spinner.position == 0


def test_unspinnable_spinner() -> None:
    """
    Makes sure that a spinner with only one slot
    doesn't cause any problems
    """
    spinner = Spinner(1)
    spinner.spin(0)
    assert spinner.position == 0
    spinner.spin(1)
    assert spinner.position == 0
    spinner.spin(99)
    assert spinner.position == 0


# This is a hypothesis test; it generates a random integer to use as input,
# so that we don't need to hard-code a specific number of slots in the test.
# For more information on hypothesis (one of the testing libraries we're using),
# please see
# https://www.teach.cs.toronto.edu/~csc148h/winter/notes/testing/hypothesis.html
@given(slots=integers(min_value=1))
def test_new_spinner_position(slots: int) -> None:
    """Test that the position of a new spinner is always 0."""
    spinner = Spinner(slots)
    assert spinner.position == 0


def test_unlike_doctest() -> None:
    """Test the given doctest in the unlike method of Tweet."""
    tweet = Tweet('Sophia', date(2021, 1, 1), 'Happy new year!')
    tweet.like(5)
    assert tweet.likes == 5
    tweet.unlike()
    assert tweet.likes == 4


def test_unlikes_no_likes() -> None:
    """
    Tests when there is an unlike but there are
    already no likes on the tweet
    Note: Should be impossible.
    """
    tweet = Tweet('Sophia', date(2021, 1, 1), 'Happy new year!')
    tweet.like(0)
    assert tweet.likes == 0
    tweet.unlike()
    assert tweet.likes == 0


if __name__ == '__main__':
    import pytest
    pytest.main(['prep2_starter_tests.py'])
