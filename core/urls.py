from django.urls import path
from .views import *


app_name = 'core'

urlpatterns = [
    path('', base, name='base'),
    path('calendar/', calendar, name='calendar'),
    path('info/<int:id>/', info, name='info'),
    path('reviews/', review, name='reviews'),
    path('review/create/', review_create, name='review_create'),
]