from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')

