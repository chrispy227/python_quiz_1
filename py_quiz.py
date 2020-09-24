from random import seed
from random import sample

# Create Individual Lists of Question Strings, Answer Choices Strings (a. choice, etc.), ANswer key string, Correct Boolean init val of False, Guesses init INteger val of 3
# List Layout: {[0]Question:"", [1]Choices:"", [2]Answer:"", [3]Correct:Boolean, [4]Guesses: int(3)}
Q1 = ["What type of aircraft is a Helicopter?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "b", False, 3]
Q2 = ["What type of aircraft is a Plane?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "a", False, 3]
Q3 = ["What type of aircraft typically has no engine?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "d", False, 3]
# Create a dictionary containing all question dictionaries
QuestionBank = dict({0: Q1, 1: Q2, 2: Q3})
# Random Selector


def randomQuestion():
    Qlist = list(QuestionBank)
    AskList = sample(Qlist, len(Qlist))
    print(AskList)
    Ask1 = AskList[0]
    print(Ask1)


randomQuestion()

# Create a Input Validator Function to:
# --Try to convert to Int, if this passes, then fails validation, Throw a custom error message and ask to try again, do not subtract from guess
# --If Conversion to Int fails, then make lowercase String and strip leading and trailing edge whitespaces

# Create function to Compare validated String value to Current Question ANSWER KEY
# -IF passes, Change Correct Boolean to TRUE
# -Allow next Question to be displayed to USer
# ---IF Fails comparison, subtract 1 from current question GUESS variable, throw Error: "Try Again: "
# ---repeat till GUESS = 0 or answered correctly

# Create Score Function to check range length, count Correct Boolean True values, and Make a Percentage of Correct/Total Questions.

# Create Function to Ask Questions from Array, displaying the question, answer choices only.
# -Use random number function to pull random question index
# -Do not allow repeats: Create an Array of Indexes already used before displaying a question
# --Use Validator Function on each question answer input
# ---Use comparison Function on each validated input to compare to current Question ANswer Key
# ASk play again after all questions in range have been asked
