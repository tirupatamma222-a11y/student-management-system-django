from django.urls import path
from .views import student_delete,student_form,student_list,student_update


urlpatterns = [
    path('',student_form),
    path('list/',student_list),
    path('update/<int:id>/',student_update),
    path('delete/<int:id>/',student_delete),
]