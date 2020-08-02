from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create/view/',views.webinarAdder.as_view()),
    path('update/view/',views.webinarModifier.as_view()),
    path('delete/view/<str:pk>/',views.webinarDelete.as_view()),
]