from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import QuizCategory, QuizQuestion, UserSubmittedAnswer
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
        category = QuizCategory.objects.get(id=cat_id)
        question = QuizQuestion.objects.filter(category=category, id__gt=quest_id).exclude(id=quest_id). \
            order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest = QuizQuestion.objects.get(id = quest_id)
                user = request.user
                answer = 'Not submitted'
                UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
                return render(request, 'category-questions.html', {'question': question, 'category': category})
        else:
            quest = QuizQuestion.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['answer']
            UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if question:
            return render(request, 'category-questions.html', {'question': question, 'category': category})
        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user)
            return render(request, 'result.html', {'result': result, 'category': category})
    else:
        return HttpResponse('Method not allowed!!!')
