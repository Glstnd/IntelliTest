from django.shortcuts import render
from . import forms
from .models import QuizCategory, QuizQuestion
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required


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
    category = QuizCategory.objects.get(id=cat_id)
    questions = QuizQuestion.objects.filter(category=category)
    return render(request, 'category-questions.html', {"questions": questions, "category": category})


def user_login(request, username, password):
    if request.method == 'POST':
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    print('login')
    return render(request, 'home.html')
