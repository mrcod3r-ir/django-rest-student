import imp
from django.urls import path
from .views import student_List

urlpatterns = [
    path("student_list",student_List)
]
