from django.contrib import admin
from .models import QuizCategory, QuizQuestion, UserSubmittedAnswer

admin.site.register(QuizCategory)


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


admin.site.register(QuizQuestion, QuizQuestionAdmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'user', 'right_answer']


admin.site.register(UserSubmittedAnswer, UserSubmittedAnswerAdmin)