from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Agents_Details
from uszipcode import SearchEngine, SimpleZipcode, Zipcode
from django.http import HttpResponse
from  geopy.geocoders import Nominatim

def home(request):
    # return HttpResponse("<h1> Subu </h1>")
    return render(request,"AgentsList/index.html")


def agentslist(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/newyork.html", {'name_of_city':name_of_city, })



def nyList(request):
    name_of_city = None
    # if request.method == 'POST':
    #     name_of_city = request.POST.get("city", "")
    ten_details = Agents_Details.objects.all().order_by('id')[0:100]


    return render(request, "AgentsList/newyork.html", {'ten_details' : ten_details, })

def btList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/boston.html", {'name_of_city':name_of_city, })

def laList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/la.html", {'name_of_city':name_of_city, })

def ccList(request):
    geolocator = Nominatim(user_agent="AgentsList")
    loc = geolocator.geocode("99501")
    qwerty = loc.latitude
    asdfg = loc.longitude
    return render(request, "AgentsList/chicago.html", {'lat':qwerty,'long':asdfg})

def htList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/houston.html", {'name_of_city':name_of_city, })

def pxList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/phoenix.html", {'name_of_city':name_of_city, })

def sjList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/sanjose.html", {'name_of_city':name_of_city, })

def csList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/columbus.html", {'name_of_city':name_of_city, })

def dsList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/dallas.html", {'name_of_city':name_of_city, })

def sdList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/sandiego.html", {'name_of_city':name_of_city, })


def atList(request):
    name_of_city = None
    if request.method == 'POST':
        name_of_city = request.POST.get("city", "")
    # ten_details = Agents_Details.objects.all()
    return render(request, "AgentsList/austin.html", {'name_of_city':name_of_city, })