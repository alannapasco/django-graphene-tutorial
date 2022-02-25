from graphene_django import DjangoObjectType
from .models import Quizzes, Category, Question, Answer


class QuizType(DjangoObjectType):
    #helps serializing the data
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "quiz", "technique")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer_text")