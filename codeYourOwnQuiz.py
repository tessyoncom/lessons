# This code is a quiz game. Users are expected to enter the correct word for any level of the game they are playing.
"""
# my algorithm is below:
# 1. Defining the quiz question levels: Easy, Medium and Hard
# 2. Create a list to blank out in each levels - 4 for each
# 3. Accept user input to choose levels they want to play.
 For each question running, accept user input and verify correctness. If correct, move to next question
otherwise, persist on same question 4 times. If after 4 trials, user unable to put the correct question,
the user loses the game. If the user input is correct at any point, display the full sentence with the correct input
to that point.

"""

# Defining quiz questions

# Easy question =  My name is Tesilimi Yusuf. I am from Lagos, Nigeria. I am trying to learn Python.

# Medium question = Nigeria is a country in West Africa. It has a population of about 180 million people.

# Hard question = Software development is quite challenging by a rewarding endeavour. You wanna  try?

easy = " My name is __1__ Yusuf. I am from __2__, Nigeria. I am trying to learn __3__."

medium = "Nigeria is a __1__ in West Africa. It has a __2__ of about 180 million __3__."

hard = "Software __1__ is quite challenging by a rewarding __2__. You wanna  __3__?"

easy_answers = [ "Tesilimi", "Lagos", "Python"]
medium_answers = [ "country", "population", "people"]
hard_answers = [ "development", "endeavour", "try"]

#function to capture user levels choice
def user_choice(choice):
    if choice == "easy":
        return "easy"
    elif choice == medium:
        return "medium:
    else:
        return "hard"


