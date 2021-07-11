from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain
from ui import QuizInterface, OptionsInterface

question_bank = []

# Prompts user for a game setup, do it again if not enough questions returned by the API
while len(question_bank) < 10:
    options = OptionsInterface()

    cat = int(options.v.get())
    dif = options.d.get()
    question_data = get_questions(cat, dif)

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
