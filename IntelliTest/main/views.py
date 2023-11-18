from django.shortcuts import render
from . import forms
from .models import QuizCategory, QuizQuestion


def home(request):
    return render(request, 'home.html')


def register(request):
    msg = None
    form = forms.RegisterUser
    if request.method == 'POST':
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been added'
    return render(request, 'registration/register.html', {'form': form, msg: 'msg'})


def all_categories(request):
    cat_data = QuizCategory.objects.all()
    return render(request, 'all-category.html', {'data': cat_data})


def category_questions(request, cat_id):
    category = QuizCategory.get(id=cat_id)
    questions = QuizQuestion.objects.get(category=category)
    return render(request, 'category-questions.html')
