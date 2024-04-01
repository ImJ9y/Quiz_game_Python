class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_question(self):
        return self.question_number < len(self.question_list)
    
    def next_Question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_score(user_answer, curr_question.answer)

    def check_score(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        
        print(f"correct answer {correct_answer}")
        print(f"{self.score}/{self.question_number}")
        