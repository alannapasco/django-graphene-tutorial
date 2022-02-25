from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]


@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'quiz',
        'title',
    ]

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'question',
        'answer_text',
        'is_right',
    ]