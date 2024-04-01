from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []

for question in question_data:
    question_bank.append(Question(text = question["question"], answer = question["correct_answer"]))

quiz = Quiz(question_bank)

while quiz.still_question():
    quiz.next_Question()

print("You've compelted the quiz")
print(f"Final score: {quiz.score}/{quiz.question_number}")