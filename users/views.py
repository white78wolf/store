from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html', {'title': "Store - Авторизация"})

def registration(request):
    return render(request, 'users/registration.html', {'title': "Store - Регистрация покупателя"})
