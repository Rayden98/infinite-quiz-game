from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quiz_Interface
import requests
import json
import time

# -------------------------- MODIFYING THE CALL ---------------------------- #
parameters = {
    "amount" :10,
    "type":"boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()
with open("data.py", "w") as data_file:
    data_file.write(f"question_data = {data['results']}")
    time.sleep(2)


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = Quiz_Interface(quiz)

# while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
