from question_model import Question
from data import api_db
from quiz_brain import QuizBrain
from ui import QuizInterface

# Initial values:
local_db = list()
# Creating the local database from API:
for question in api_db:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    question_ready = Question(q_text, q_answer)
    local_db.append(question_ready)  # from API db, adding each available question and its answer in local db.


quiz = QuizBrain(local_db)
quiz_ui = QuizInterface(quiz)  # calling the user interface.

# while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
