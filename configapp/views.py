from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    news = News.objects.all()
    categories = Categories.objects.all()

    context = {
        "news":news,
        "categories":categories,
    }
    return render(request,'index.html',context=context)
def categories(request,category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Categories.objects.all()

    context = {
        "news":news,
        "categories":categories,
    }
    return render(request,'categories.html',context=context)

def new_about(request,new_id):
    new = News.objects.get(pk=new_id)
    categories = Categories.objects.all()

    context = {
        "new": new,
        "categories": categories,
    }
    return render(request, 'new_about.html', context=context)

def add_news(request):
    print(request)
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, "add_news.html", {"form": form})



def add_categories(request):
    print(request)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            user = Categories.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, "add_categories.html", {"form": form})

def update_news(request,new_id):
    new = get_object_or_404(News,id=new_id)
    if request.method=="POST":
        form = NewsForm(request.Post,instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = NewsForm(instance=new)
        return render(request,'update_new.html',{'form':form,"new":new})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form})
def search_news(request):
    query = request.GET.get("q", "")
    results = list(News.objects.filter(title__icontains=query).values_list("id","title")[:5]) if query else []
    return JsonResponse({"results": results})