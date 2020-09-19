from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render

from django.http import HttpResponse
def home(request):
    # return HttpResponse("<h1> Subu </h1>")
    return render(request,"AgentsList/index.html")