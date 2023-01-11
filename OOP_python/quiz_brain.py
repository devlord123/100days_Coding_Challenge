class QuizBrain:
    def __init__(self, list):
        self.question_num = 0
        self.score = 0
        self.list = list

    def more_ques(self):
        return self.question_num < len(self.list)

    def next_question(self):
        c_quest = self.list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}: {c_quest.question} (True/False) ")
        self.check_answer(user_ans, c_quest.answer)

    def check_answer(self, user, answer):
        if user.lower() == answer.lower():
            self.score += 1
            print('You got it!')
        else:
            print("Wrong answer dude")
        print(f"Your total score is {self.score}/{self.question_num}")
