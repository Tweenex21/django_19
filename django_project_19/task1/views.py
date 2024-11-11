from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *

# Create your views here.


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            users = Buyer.objects.values_list('name', flat=True)
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=100.00, age=age)
                info['message'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()
    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        users_info = Buyer.objects.all()
        users = [user.name for user in users_info]
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=username, balance=200.00, age=age)
            info['message'] = f'Приветствуем, {username}!'
    return render(request, 'first_task/registration_page.html', info)


def platform_tmpl(request):
    title = 'Главная'
    page = 'Главная страница'
    context = {
        'title': title,
        'page': page
    }
    return render(request, 'first_task/platform.html', context)


def cart_tmpl(request):
    title = 'Корзина'
    page = 'Корзина'
    context = {
        'title': title,
        'page': page
    }
    return render(request, 'first_task/cart.html', context)


def games_tmpl(request):
    title = 'Магазин'
    page = 'Игры'
    context = {
        'title': title,
        'page': page,
        'games': Game.objects.all()
    }
    return render(request, 'first_task/games.html', context)
