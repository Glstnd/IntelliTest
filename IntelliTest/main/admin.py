from django.contrib import admin
from .models import QuizCategory, QuizQuestion

admin.site.register(QuizCategory)


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


admin.site.register(QuizQuestion, QuizQuestionAdmin)
