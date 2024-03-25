from django.http import HttpResponse
from django.shortcuts import render


MENU = {"Главная": "/", "Каталог":"/catalog", "О сайте":"/about"}

def main_page(request):
    title = "Главная страница"
    data = {"title": title, "menu":MENU }
    return render(request, "./index.html",context=data)

def about_page(request):
    title = "О компании"
    data = {"title": title, "menu":MENU }
    return render(request, "./about.html",context=data)

