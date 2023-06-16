from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def create_letter(request):
    return render(request, "create_letter.html")

def list_letter(request):
    return render(request, "list_letter.html")

def detail_letter(request,letter_id):
    return render(request, "detail_letter.html")

def success_letter(request):
    return render(request, "success_letter.html")