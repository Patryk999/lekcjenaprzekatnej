from django.contrib import admin
from django.urls import path

from course import views
urlpatterns = [
    path('<str:name>/<int:id_of_class>/', views.course_all_page, name='course_all'),
    path('<str:name>/<int:id_of_class>/<int:id_of_course>/', views.course, name='course'),
    path('<str:name>/', views.class_all_page, name='class_all'),
    path('', views.subject_all_page, name='subject_all')
]
