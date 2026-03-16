from flask import Flask, render_template, request
from datetime import datetime
from models import Question

app = Flask(__name__)

# Stack to store answered questions
answered_stack = []

questions = [
    Question("What is 2 + 2?", ["1","2","3","4"], "4"),
    Question("Capital of Nigeria?", ["Lagos","Abuja","Kano","Ibadan"], "Abuja"),
    Question("Which language is used with Flask?", ["Java","Python","C++","PHP"], "Python")
]

@app.route("/")
def home():
    return render_template("quiz.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():

    score = 0

    for i, q in enumerate(questions):

        user_answer = request.form.get(f"q{i}")

        answered_stack.append(user_answer)

        if q.check_answer(user_answer):
            score += 1

    submission_time = datetime.now()

    return render_template(
        "result.html",
        score=score,
        total=len(questions),
        time=submission_time
    )

if __name__ == "__main__":
    app.run(debug=True)