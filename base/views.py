from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def createQuestion(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        formulario = QuestionForm(request.POST)

        print(formulario)

    else:

        formulario = QuestionForm()

        return render(request, "QuestionForm.html", {"formulario": formulario})
