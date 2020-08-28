#! python3
# LearnMultiplication.py - Game to help improve multiplication.

import random as r

correct_tally = 0
tested_nums = []  # nums already tested

while True:
    try:
        TOTAL_TESTS = int(input("Enter total number times you want to be tested: "))
        tests_remaining = TOTAL_TESTS
        break
    except ValueError:
        print("Please enter a number!")

while True:
    try:
        MAX_MULTIPLIER = int(input("Enter maximum number to multiply: "))
        break
    except ValueError:
        print("Please enter a number!")


def create_r_num():
    #   creates random interger between 1 to input

    a = 1
    b = MAX_MULTIPLIER
    # b = 10
    return r.randint(a, b)


while tests_remaining > 0:
    num_1 = create_r_num()
    num_2 = create_r_num()
    answer = num_1 * num_2
    tests_remaining -= 1
    errors = 0
    MAX_ERROR = 2

    while True:  # if incorrect

        while True:  # check number is correct
            try:
                enter_answer = int(input("%s x %s = " % (num_1, num_2)))
                break
            except ValueError:
                print("Please enter a number!")

        if enter_answer == answer:
            correct_tally += 1
            print('Correct!')
            break
        else:
            if errors == MAX_ERROR:
                print('Incorrect. Answer: %s'%(answer))
                break
            else:
                print('Incorrect. Try again! Remaining attempts: %s'%(MAX_ERROR - errors))
                errors += 1

print("You completed the test. Good on you!")
