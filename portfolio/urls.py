from django.urls import path
from .views import *

urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/categories/<int:cat_id>/', show_categories, name='categories'),
]
