from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name='register'),
    path('all-categories', views.all_categories, name='all_categories'),
    path('category-questions/<int:cat_id>', views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', views.submit_answer, name='submit_answer'),
    path('result/', views.result, name='result'),
    path('result/<int:cat_id>', views.result_category, name='result_category'),
    path('create-test/', views.create_test, name='create_test'),
    path('change-test/<int:cat_id>', views.change_test, name='change_test'),
    path('change-test/<int:cat_id>/<int:quest_id>', views.change_quest_test, name='change_quest_test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
