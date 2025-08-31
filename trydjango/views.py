from django.shortcuts import render
from articles.models import Article

def home(request):
    return render(request, "pages/home.html")
