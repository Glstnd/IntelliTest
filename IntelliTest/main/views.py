from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import QuizCategory, QuizQuestion, UserSubmittedAnswer
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def user_page(request):
    return render(request, 'user.html')


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
    UserSubmittedAnswer.objects.filter(category=category).delete()
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
                UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer, category=category)
                return render(request, 'category-questions.html', {'question': question, 'category': category})
        else:
            quest = QuizQuestion.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['answer']
            UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer, category=category)
        if question:
            return render(request, 'category-questions.html', {'question': question, 'category': category})
        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user, category=category)
            skipped = UserSubmittedAnswer.objects.filter(user=request.user, right_answer='Not submitted',
                                                         category=category).count()
            attempted = UserSubmittedAnswer.objects.filter(user=request.user, category=category).exclude(right_answer='Not submitted').count()
            rightAns = 0
            percentage = 0
            for row in result:
                if row.question.right_opt == row.right_answer:
                    rightAns += 1
            percentage = (rightAns*100)/result.count()
            return render(request, 'result_category.html', {'category': category, 'result': result, 'skipped': skipped, 'attempted': attempted, 'rightAns': rightAns, 'percentage': percentage})
    else:
        return HttpResponse('Method not allowed!!!')


@login_required
def result(request):
    categories = QuizCategory.objects.all()
    return render(request, 'result.html', {'categories': categories})


@login_required
def result_category(request, cat_id):
    categories = QuizCategory.objects.all()
    category = QuizCategory.objects.get(id=cat_id)
    result = UserSubmittedAnswer.objects.filter(user=request.user, category=category)
    if result.count() == 0:
        return render(request, 'result.html',
                      {'result': result, 'skipped': 0, 'attempted': 0, 'rightAns': 0,
                       'percentage': 0})
    skipped = UserSubmittedAnswer.objects.filter(user=request.user, right_answer='Not submitted',
                                                 category=category).count()
    attempted = UserSubmittedAnswer.objects.filter(user=request.user, category=category).exclude(right_answer='Not submitted').count()
    rightAns = 0
    percentage = 0
    for row in result:
        if row.question.right_opt == row.right_answer:
            rightAns += 1
    percentage = (rightAns * 100) / result.count()
    return render(request, 'result_category.html',
                  {'category': category, 'result': result, 'skipped': skipped, 'attempted': attempted, 'rightAns': rightAns,
                   'percentage': percentage})


@login_required
def create_test(request):
    categories = QuizCategory.objects.all()
    return render(request, 'form-test.html', {'categories': categories})


@login_required
def change_test(request, cat_id):
    print(request.method)
    if request.method == "POST":
        new_cat_name = request.POST.get("cat_name")
        new_cat_details = request.POST.get("cat_details")

        category = QuizCategory.objects.get(id=cat_id)
        category.title = new_cat_name
        category.details = new_cat_details
        category.save()
    if cat_id == 0:
        categories = QuizCategory.objects.all()
        QuizCategory.objects.create(title=f'Тест {len(categories)}')
        return redirect('create_test')
    category = QuizCategory.objects.get(id=cat_id)
    questions = QuizQuestion.objects.filter(category=category)
    return render(request, 'change_test_form.html', {'category': category, 'questions': questions})


@login_required
def change_quest_test(request, cat_id, quest_id):
    category = QuizCategory.objects.get(id=cat_id)
    if quest_id == 0:
        QuizQuestion.objects.create(category=category, question=f'Вопрос...', opt_1='Ответ', opt_2='Ответ',
                                    opt_3='Ответ', opt_4='Ответ', level='begginer', right_opt='Ответ', time_limit=300)
        questions = QuizQuestion.objects.filter(category=category)
        return render(request, 'change_test_form.html', {'category': category, 'questions': questions})
    questions = QuizQuestion.objects.filter(category=category)
    question = QuizQuestion.objects.get(id=quest_id)
    if request.method == 'POST':
        question.question = request.POST.get("question")
        question.opt_1 = request.POST.get("opt_1")
        question.opt_2 = request.POST.get("opt_2")
        question.opt_3 = request.POST.get("opt_3")
        question.opt_4 = request.POST.get("opt_4")
        question.right_opt = request.POST.get("right_opt")
        question.save()

    return render(request, 'change_question_form.html', {'category': category, 'questions': questions,
                                                         'active_question': question})
