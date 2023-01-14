from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    f_question = question["question"]
    f_answer = question["correct_answer"]
    new_question = Question(f_question, f_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.more_ques():
    quiz.next_question()
print("You've completed the quiz")
