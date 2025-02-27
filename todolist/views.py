from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    oi = [5,23,4,7,6]

    return render(request, "todolist/index.html", {"oi":oi})