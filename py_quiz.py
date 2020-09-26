from random import seed
from random import sample

# List intended Layout: {[0]Question:"", [1]Choices:"", [2]Answer:"", [3]Correct:Boolean, [4]Guesses: int(3)}
Q1 = ["What type of aircraft is a Helicopter?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "b"]
Q2 = ["What type of aircraft is a Plane?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "a"]
Q3 = ["What type of aircraft typically has no engine?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "d"]
Q4 = ["What type of aircraft is reliant on wind currents for direction control?",
      "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "c"]
# Create a dictionary containing all question dictionaries
QuestionBank = dict({0: Q1, 1: Q2, 2: Q3, 3: Q4})


def quiz():
    # Make a Random list from Question bank.
    # Random Selector
    def random_question():
        # Convert QuestionBank Dictionary to a List
        Qlist = list(QuestionBank)
        # Creates a random ordered list with integers as values to be used to pick questions in another function
        global RandAskList
        RandAskList = sample(Qlist, len(Qlist))
        # This is only for question selection and cannot double index to the question lists
    random_question()

    def validate_input():
        while True:
            value = input("Please enter the letter choice for your answer: ")
            if value.lower().strip() not in ('a', 'b', 'c', 'd'):
                print("Sorry, your response must be A, B, C, or D. Please Try Again.")
                continue
            else:
                break
        return value
    # Initialize the Sentry
    finishedQuestions = 0
    Score = 0
    scoreDenominator = "/{}"
    numQuestions = len(QuestionBank)
    while finishedQuestions < numQuestions:
        keyIndex = RandAskList[finishedQuestions]
        correctKey = QuestionBank[keyIndex][2]
        print(QuestionBank[RandAskList[finishedQuestions]][0])
        print(QuestionBank[RandAskList[finishedQuestions]][1])
        valdGuess = validate_input()
        while valdGuess:
            if valdGuess == (correctKey):
                print("That is Correct! Good Job!")
                Score += 1
                valdGuess = None
            else:
                print("Sorry, that is Wrong.")
                valdGuess = None
                break
        finishedQuestions += 1
        if finishedQuestions == numQuestions:
            if Score == numQuestions:
                print("YOU WIN WITH A PERFECT SCORE!!!!")
            else:
                print("You Scored: ")
            print(str(Score) + scoreDenominator.format(numQuestions))


quiz()









