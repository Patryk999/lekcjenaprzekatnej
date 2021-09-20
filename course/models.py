from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Subject(models.Model):
    subject_title = models.CharField(max_length=200)
    order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.subject_title}"


class Class(models.Model):
    class_title = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.subject_title} {self.class_title}"


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    class_foreign_key = models.ForeignKey(Class, default=None, on_delete=models.CASCADE)
    number_of_entries = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.course_title}"


class Question(models.Model):
    question = models.CharField(max_length=250)
    image_question = models.ImageField(blank=True, null=True, upload_to="images/")
    image_answer = models.ImageField(blank=True, null=True, upload_to="images/")
    answer_1 = models.CharField(max_length=50)
    answer_2 = models.CharField(max_length=50)
    answer_3 = models.CharField(max_length=50)
    answer_4 = models.CharField(max_length=50)
    good_answer = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(4), MinValueValidator(1)])
    order = models.IntegerField(default=1)
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.course.class_foreign_key}: {self.question}"


