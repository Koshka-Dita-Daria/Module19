from django.shortcuts import render
from task1.models import Buyer, Game
from django.db.models import Count
from django.http import HttpResponse
from task1.forms import UserRegister
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def func1(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


def func2(request):
    title = 'Игры'
    Games = Game.objects.all()
    l4 = "Купить"
    context = {
        'title': title,
        'Games': Games,
        'l4': l4,
    }
    return render(request, 'games.html', context)


def func3(request):
    title = 'Извините, у вас 0 на счету'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)
# import random
# Create your views here.
# B_more_18 = Buyer.objects.filter(age__gte=18)
# B_less_18 = Buyer.objects.exclude(age__gte=18)
# G_with_18 = Game.objects.filter(age_limited__exact=True)
# G_kids = Game.objects.filter(age_limited__exact=False)
# stats = Game.objects.aggregate(
#     total_cost=Count('balance')
# )
# print(stats["total_cost"])
# for games in G_kids:
#     Game.objects.get(games.id).buyer.set(B_less_18)
# for games1 in G_with_18:
#     Game.objects.get(games1.id).buyer.set(B_more_18)
# k = 0
# for gamers in B_more_18:
#     for games in G_kids:
#         if gamers.balance >= stats("total_cost") and k == 0:
#             Game.objects.get(games1.id).buyer.get(gamers.id)
#     k=1
#     if k == 1:
#         break


def control(username, password, repeat_password, age, users):
    info = {}
    users = Buyer.objects.all()
    for k in users:
        if k.name == username:
            info = "Пользоатель существует"
            return info
    if password != repeat_password:
        info = "Пароли не совпадают"
        return info
    elif int(age) < 18:
        info = "Вы должны быть старше 18"
        return info
    Buyer.objects.create(name=username, balance=1000, age=age)
    info = f'Приветствуем {username}'
    return info

# def sign_up_by_html(request):
#     users = ["Linda", "Sarah", "kolin"]
#     info = {}
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#         str = control(username, password, repeat_password, age, users)
#         info = {"error": str}
#         return render(request, 'registration_page.html', info)
#     info = {}
#     return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            str = control(username, password, repeat_password, age, users)
            info = {"error": str}
            return render(request, 'registration_page.html', info)
        Buyer.objects.create(name=username, balance=10000, age=age)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})




