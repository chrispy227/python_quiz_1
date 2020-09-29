from random import sample


class QUIZ:
    """A Customizable Quiz using a 2D list to store the questions, answer choices and answer key."""

    def __init__(self, questions, topic):
        self.questions = questions  # Question 2D List
        self.topic = topic  # topic decription String

    def question_randomizer(self, questions):
        return sample(questions, len(questions))

    def question_printer(self, questions, index):
        print(questions[index][0])
        print(questions[index][1])
        print("\n")

    def validate_input(self):
        while True:
            value = input(
                "Please enter the letter choice for your answer: " + "\n")
            validInput = value.lower().strip()
            if validInput not in ('a', 'b', 'c', 'd'):
                print("Sorry, your response must be A, B, C, or D. Please Try Again.\n")
                continue
            else:
                break
        return validInput

    def run_quiz(self, questions):
        randomized_questions = self.question_randomizer(questions)
        finishedQuestions = 0
        Score = 0
        scoreDenominator = "/{}"
        numQuestions = len(randomized_questions)
        while finishedQuestions < numQuestions:
            correctKey = (randomized_questions[finishedQuestions][2])
            self.question_printer(randomized_questions, finishedQuestions)
            valdGuess = self.validate_input()
            while valdGuess:
                if valdGuess == (correctKey):
                    print("That is Correct! Good Job!\n")
                    Score += 1
                    valdGuess = None
                else:
                    print("Sorry, that is Wrong.\n")
                    valdGuess = None
                    break
            finishedQuestions += 1
            if finishedQuestions == numQuestions:
                if Score == numQuestions:
                    print("YOU WIN WITH A PERFECT SCORE!!!!")
                else:
                    print("You Scored: ")
                print(str(Score) + scoreDenominator.format(numQuestions)+"\n")


question_bank = [
    ["What type of aircraft is a Helicopter?",
     "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "b"],
    ["What type of aircraft is a Plane?",
     "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "a"],
    ["What type of aircraft typically has no engine and must be towed initially?",
     "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider\n", "d"],
    ["What type of aircraft is reliant on wind currents for direction control?",
     "A.) Fixed Wing\nB.) Rotary Wing\nC.) Hot Air Ballon\nD.) Glider", "c"]
]


quiz_1 = QUIZ(question_bank, "Aircraft Types")
quiz_1.run_quiz(question_bank)
