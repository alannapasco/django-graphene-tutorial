from .models import Quizzes, Category, Question, Answer

def resolve_all_quizzes(root, info):
    return Quizzes.objects.all()

def resolve_a_quiz(root, info, id):
    return Quizzes.objects.get(pk=id)

def resolve_all_categories(root, info):
    return Category.objects.all()

def resolve_all_questions(root, info):
    return Question.objects.all()

def resolve_all_answers(root, info):
    return Answer.objects.all()

def resolve_an_answer(root, info, id):
    return Answer.objects.get(pk=id)

def resolve_all_answers_to_question_x(root, info, question_id):
    return Answer.objects.filter(question=question_id)
