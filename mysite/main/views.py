from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpRequest
from .forms import DataForm, UserForm, QuestionForm, MailForm, PasswordForm, SupportForm
import requests
from django.contrib.auth.models import User
from .models import UserUpgrade, SupportModel
from django.contrib import auth

local = 'http://127.0.0.1:8000/'

def main_page(request):
    if request.method == 'POST':
        question = HttpRequest.body
        response = requests.post('http://192.168.43.232:8800/', data=question)
        result = response.text
    else:
        result = " "
    return render(request, 'main/index.html', {'result': result})


def about(request):
    return render(request, 'main/about.html')


def profile(request):
    return render(request, 'main/profile.html')


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            mail = form.cleaned_data.get("mail")
            user = User.objects.create_user(name, mail, password)
            user.save()
            for model in UserUpgrade.objects.all():
                if model.user == user:
                    model.question = form.cleaned_data['question']
                    model.answer = form.cleaned_data['answer']
                    model.save()
                    break
        return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserForm()
    return render(request, 'main/regis.html', {'form': form})


def reset(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            k = 0
            for user in User.objects.all():
                if user.email == mail:
                    return redirect(str(mail))
                else:
                    k += 1
            if k == len(User.objects.all()):
                error = "Вы не зарегистрированы"
    else:
        form = MailForm()
        error = ''
    return render(request, 'main/reset.html', {'form': form, 'error': error})


def reset_2(request, mail):
    for user in User.objects.all():
        if user.email == mail:
            use = user
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            models = UserUpgrade.objects.all()
            for model in models:
                if model.user == use:
                    ans = model.answer
                    ques = model.question
                    break
            if ans == form.cleaned_data['answer']:
                auth.login(request, use)
                return redirect(str(local)+'password-change/')
            else:
                error = "Неправильный ответ"
    else:
        models = UserUpgrade.objects.all()
        for model in models:
            if model.user == use:
                ques = model.question
                form = QuestionForm()
        error = ''
    return render(request, 'main/reset_2.html', {'form': form, 'ques': ques, 'error': error})


def change_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(local)
    else:
        form = PasswordForm()
    return render(request, 'main/change_password.html', {'form': form})


def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            SupportModel.objects.create(user=request.user, text=form.cleaned_data['text'])
            return redirect(local)
    else:
        form = SupportForm()
    return render(request, 'main/support.html', {'form': form})