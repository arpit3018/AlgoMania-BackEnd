from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import QuestionForm


def questionView(request):
    if request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            description = form.cleaned_data['description']
            questiontags = form.cleaned_data['questiontags']
            codesnippets = form.cleaned_data['codesnippets']

    return render(request, "question.html", {'form': form})


def submitView(request):
    return HttpResponse('You have successfully submitted the Question.')
