from django.contrib import admin

from .models import Course, Question, Subject, Class

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Class)

