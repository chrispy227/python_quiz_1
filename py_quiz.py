from random import seed
from random import sample

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
    # Convert QuestionBank Dictionary to a List
    Qlist = list(QuestionBank)
    global RandAskList
    # Creates a random ordered list with integers as values to be used to pick questions in another function
    RandAskList = sample(Qlist, len(Qlist))
    # This is only for question selection and cannot double index to the question lists


# Create a Input Validator Function to:
# --Try to convert to Int, if this passes, then fails validation, Throw a custom error message and ask to try again, do not subtract from guess
# --If Conversion to Int fails, then make lowercase String and strip leading and trailing edge whitespaces


def Quiz():
    # Make a Random list from Question bank.
    randomQuestion()
    # Initialize the Sentry
    finishedQuestions = 0
    Score = 0
    scoreDenominator = "/{}"
    while finishedQuestions < len(RandAskList):
        keyIndex = RandAskList[finishedQuestions]
        correctKey = QuestionBank[keyIndex][2]
        print(QuestionBank[RandAskList[finishedQuestions]][0])
        print(QuestionBank[RandAskList[finishedQuestions]][1])
        guess = input("Please enter the letter choice for your answer: ")
        valdGuess = guess.lower().strip()
        while valdGuess:
            if valdGuess in ["a", "b", "c", "d"]:
                print(valdGuess)
            if valdGuess == (correctKey):
                print("YOU WIN MFER!!!!")
                Score += 1
                valdGuess = None
                print(str(Score) + scoreDenominator.format(len(RandAskList)))

        finishedQuestions += 1


Quiz()

# Create function to Compare validated String value to Current Question ANSWER KEY
# -IF passes, Change Correct Boolean to TRUE
# -Allow next Question to be displayed to USer
# ---IF Fails comparison, subtract 1 from current question GUESS variable, throw Error: "Try Again: "
# ---repeat till GUESS = 0 or answered correctly

# Create Score Function to check range length, count Correct Boolean True values, and Make a Percentage of Correct/Total Questions.

# --Use Validator Function on each question answer input
# ---Use comparison Function on each validated input to compare to current Question ANswer Key
# ASk play again after all questions in range have been asked
