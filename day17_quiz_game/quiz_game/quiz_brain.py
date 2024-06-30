# TODO: 1: asking the question
# TODO: 2: checking if the answer was correct
# TODO: 3: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = input(f"Q.{self.question_number} {current_question.question} (True/False): ")
        self.check_answer(question, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong!")
        print(f"The correct answer was: {self.question_list[self.question_number-1].answer}")
        print(f"he current score: {self.score}/{self.question_number}")
        print("\n")
