from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name='register'),
    path('all-categories', views.all_categories, name='all_categories'),
    path('category-questions/<int:cat_id>', views.category_questions, name='category_questions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
