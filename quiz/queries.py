import graphene
from quiz.types import AnswerType, CategoryType, QuestionType, QuizType
from quiz.resolvers import (
    resolve_all_quizzes,
    resolve_a_quiz,
    resolve_all_categories,
    resolve_all_questions,
    resolve_all_answers,
    resolve_an_answer,
    resolve_all_answers_to_question_x,
)

#list of ALL queries related to quizzes!
class QuizQueries(graphene.ObjectType):
    all_quizzes = graphene.List(QuizType)
    def resolve_all_quizzes(root, info):
        return resolve_all_quizzes(root, info)

    a_quiz = graphene.Field(QuizType, id=graphene.Int())
    def resolve_a_quiz(root, info, id):
        return resolve_a_quiz(root, info, id)


#list of ALL queries related to Categories!
class CategoryQueries(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(root, info):
        return resolve_all_categories(root, info)


#list of ALL queries related to Questions!
class QuestionQueries(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)

    def resolve_all_questions(root, info):
        return resolve_all_questions(root, info)


#list of ALL queries related to Answers!
class AnswerQueries(graphene.ObjectType):
    all_answers = graphene.List(AnswerType)
    def resolve_all_answers(root, info):
        return resolve_all_answers(root, info)

    an_answer = graphene.Field(AnswerType, id=graphene.Int())
    def resolve_an_answer(root, info, id):
        return resolve_an_answer(root, info, id)

    all_answers_to_question_x = graphene.List(AnswerType, question_id=graphene.Int())
    def resolve_all_answers_to_question_x(root, info, question_id):
        return resolve_all_answers_to_question_x(root, info, question_id)
