from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import interface
import time


start = time.time()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = interface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

end = time.time()
time = end - start
print(f"Total Quiz duration: {time:02f}sec")
