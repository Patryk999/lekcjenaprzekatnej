from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from course.models import Course, Question, Class, Subject
from django.http import HttpResponse

# Create your views here.


def subject_all_page(request):
    objects = Subject.objects.all().order_by('order')
    return render(request, "course/subject_all_page.html", {"subjects": objects})


def class_all_page(request, name):
    subject_of_class = get_object_or_404(Subject, subject_title=name)
    classes = Class.objects.all().filter(subject=subject_of_class.id).order_by('order')
    return render(request, 'course/class_all_page.html', {"name": name, "objects": classes})


def course_all_page(request,name, id_of_class):
    course_class = get_object_or_404(Class, id=id_of_class)
    objects = Course.objects.all().filter(class_foreign_key=id_of_class).order_by('order')
    return render(request, 'course/course_all_page.html', {"course_class": course_class,
                                                           "objects": objects, "subject_name": name})


def course(request, name, id_of_class, id_of_course):
    object = get_object_or_404(Course, pk=id_of_course)
    questions = Question.objects.all().filter(course=id_of_course).order_by('order')
    course_class = get_object_or_404(Class, id=id_of_class)
    if request.method =="POST":
        num = 1
        q = dict()
        for x in questions:
            c = str('button' + str(x.id))
            if c in request.POST:
                selected_option = request.POST[str('button' + str(x.id))]
            else:
                selected_option = '0'
            num += 1
            q[x] = int(selected_option)

        score = 0
        for x in q.items():
            if x[0].good_answer == x[1]:
                score+=1

        dictr = dict()
        dictr["id"] = id_of_class
        dictr["object"] = object
        dictr["questions"] = q
        dictr["score"] = score
        dictr["num_of_items"] = len(q)
        dictr["subject_name"] = name
        dictr["course_class"] = course_class

        object.number_of_entries += 1
        object.save()

        return render(request, 'course/answers_page.html', dictr)

    return render(request, 'course/course_page.html', {"id": id_of_class, "object": object,
                                                       "subject_name": name, "questions": questions,
                                                       "course_class": course_class})
