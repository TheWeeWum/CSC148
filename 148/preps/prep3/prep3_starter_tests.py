"""CSC148 Prep 3: Inheritance

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu, Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 David Liu, Sophia Huynh

=== Module description ===
This module contains sample tests for Prep 3.
Complete the TODO in this file.

There is also a task inside prep3.py.
Make sure to look at that file and complete the TODO there as well.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here
"""
from datetime import date
from hypothesis import given
from hypothesis.strategies import integers, floats
from prep3 import SalariedEmployee, HourlyEmployee, Company


################################################################################
# Part 3
# In this part, you will be writing your own test cases from scratch.
# You must implement *at least* 2 more test cases to test your code.
# 
# These test cases must be in their own functions, their names must start 
# with "test_", and the test names must be unique.
#
# These test cases must pass on a working version of the prep3 code 
# (i.e. a working version of SalariedEmployee, HourlyEmployee, Company) and
# must create at least one SalariedEmployee or HourlyEmployee.
#
# You must NOT access any private variables.
#       
# There are no other requirements for the test cases.
#
# You can verify whether your test cases are acceptable by running the
# automated tests on MarkUs.
################################################################################
# TODO: Implement *at least* 2 more test cases to test your code.


# === Sample test cases below ===
# Use the below test cases as an example for writing your own test cases,
# and as a start to testing your prep3.py code.

# WARNING: THIS IS CURRENTLY AN EXTREMELY INCOMPLETE SET OF TESTS!
# We will test your code on a much more thorough set of tests!
def test_total_pay_basic() -> None:
    e = SalariedEmployee(14, 'Gilbert the cat', 1200.0)
    e.pay(date(2018, 6, 28))
    e.pay(date(2018, 7, 28))
    e.pay(date(2018, 8, 28))
    assert e.total_pay() == 300.0


def test_total_payroll_mixed() -> None:
    my_corp = Company([SalariedEmployee(24, 'Gilbert the cat', 1200.0),
                       HourlyEmployee(25, 'Chairman Meow', 500.25, 1.0)])
    my_corp.pay_all(date(2018, 6, 28))
    assert my_corp.total_payroll() == 600.25


def test_no_pay() -> None:
    e = SalariedEmployee(0, "Name", 0.0)
    e.pay(date(2018, 6, 28))
    assert e.total_pay() == 0.0


def test_variable_pay() -> None:
    e = HourlyEmployee(0, "Name", 20.0, 160)
    e.pay(date(2018, 6, 28))
    e.hourly_wage = 22.0
    e.hours_per_month = 140
    e.pay(date(2018, 7, 28))
    assert e.total_pay() == 6280.0



if __name__ == '__main__':
    import pytest
    pytest.main(['prep3_starter_tests.py'])
