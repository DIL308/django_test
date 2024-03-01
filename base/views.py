from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def createQuestion(request):

    # print('method: ', request.method)
    # print('post: ', request.POST)

    if request.method == 'POST':

        formulario = QuestionForm(request.POST)


        if formulario.is_valid():

            data = formulario.cleaned_data

            question = Question(question_text=data['question_text'], pub_date=data['pub_date'])
            question.save()


            return HttpResponse('Guardado con éxito')

        else:
          
          return HttpResponse('Formulario Inválido')     

        

    else:

        formulario = QuestionForm()

        return render(request, "QuestionForm copy.html", {"formulario": formulario})
