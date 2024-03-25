from django.shortcuts import render
from .models import Product, ProductComment


menu = {"Главная": "/", "Каталог":"/catalog", "О сайте":"/about"}


def catalog_page(request):
    products = Product.objects.all()
    title = "Каталог"
    data = {"title": title, "menu": menu, "products": products}
    return render(request, "./catalog.html",context=data)


def add_comment_page(request):
    products = Product.objects.values("id", "name")
    title = "Добавить комментарий"
    data = {"title": title, "menu": menu, "products": products}
    return render(request, "./add_comment.html",context=data)


def thanks_page(request):
    user_name = request.POST['user_name']
    comment = request.POST['comment']
    product = Product.objects.get(pk=request.POST['product'])
    ProductComment.objects.create(user_name=user_name, comment=comment, product=product)
    title = "Страница благодарности"
    data = {"title": title, "menu": menu, "user_name":user_name}
    return render(request, "./thanks.html", context=data)




