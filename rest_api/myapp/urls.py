import imp
from django.urls import path
from .views import student_List,student_Details

urlpatterns = [
    path("student_list",student_List),
    path('student_details/<pk>',student_Details)
]
