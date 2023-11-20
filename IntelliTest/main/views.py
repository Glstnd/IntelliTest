from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import QuizCategory, QuizQuestion
from django.contrib.auth.decorators import login_required


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


@login_required
def category_questions(request, cat_id):
    category = QuizCategory.objects.get(id=cat_id)
    question = QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'category-questions.html', {'question': question, 'category': category})


@login_required
def submit_answer(request, cat_id, quest_id):
    if request.method == 'POST':
        if 'skip' in request.POST:
            return HttpResponse('Skip is clicked!!!')
        category = QuizCategory.objects.get(id=cat_id)
        question = QuizQuestion.objects.filter(category=category).order_by('id').first()
        return render(request, 'category-questions.html', {'question': question, 'category': category})
    else:
        return HttpResponse('Method not allowed!!!')
