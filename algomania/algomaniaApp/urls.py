from django.contrib import admin
from django.urls import path

from .views import questionView, submitView

urlpatterns = [

    path('question/', questionView, name='question'),
    path('submit/', submitView, name='submit'),
]
