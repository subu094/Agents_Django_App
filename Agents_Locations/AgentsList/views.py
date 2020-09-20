from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Agents_Details
from  geopy.geocoders import Nominatim
from geopy import  distance



def home(request):
    # return HttpResponse("<h1> Subu </h1>")
    return render(request,"AgentsList/index.html")


def nearest_city_list(city_name):
    geolocator = Nominatim(user_agent="AgentsList")
    loc1 = geolocator.geocode(city_name)
    coordinate_1 = (loc1.latitude, loc1.longitude)
    x = Agents_Details.objects.all()
    agent_dict = {}
    for i in x:
        # loc = geolocator.geocode(i.zipcode)
        coordinate_2 = (i.latitude, i.longitude)
        adist = distance.geodesic(coordinate_1, coordinate_2).km
        agent_dict[i.name, i.address, i.city, i.state, i.zipcode] = adist

    sorted_dict = {k: v for k, v in sorted(agent_dict.items(), key=lambda item: item[1])}
    nearestAgentstList = {k: sorted_dict[k] for k in list(sorted_dict)[:100]}
    return nearestAgentstList



def nyList(request):
    New_York_City_List = nearest_city_list(' New york city, New york')
    return render(request, "AgentsList/newyork.html", {'distance_result': New_York_City_List})

def btList(request):
    Boston_List = nearest_city_list('Boston, Massachusetts')
    return render(request, "AgentsList/boston.html", {'distance_result': Boston_List})

def laList(request):
    LA_List = nearest_city_list('Los Angeles, California')
    return render(request, "AgentsList/la.html", {'distance_result': LA_List})

def ccList(request):
    Chicago_List = nearest_city_list('Chicago, Illinois')
    return render(request, "AgentsList/chicago.html", {'distance_result':Chicago_List})

def htList(request):
    Houston_List = nearest_city_list('Houston, Texas')
    return render(request, "AgentsList/houston.html", {'distance_result': Houston_List})

def pxList(request):
    Phoenix_List = nearest_city_list('Phoenix, Arizona')
    return render(request, "AgentsList/phoenix.html", {'distance_result': Phoenix_List})

def sjList(request):
    San_Jose_List = nearest_city_list('San Jose, California')
    return render(request, "AgentsList/sanjose.html", {'distance_result': San_Jose_List})

def csList(request):
    Columbus_List = nearest_city_list('Columbus, Ohio')
    return render(request, "AgentsList/columbus.html", {'distance_result': Columbus_List})

def dsList(request):
    Dallas_List = nearest_city_list('Dallas, Texas')
    return render(request, "AgentsList/dallas.html", {'distance_result': Dallas_List})

def sdList(request):
    San_Diego_List = nearest_city_list('San Diego, California')
    return render(request, "AgentsList/sandiego.html", {'distance_result': San_Diego_List})


def atList(request):
    Austin_List = nearest_city_list('Austin, Texas')
    return render(request, "AgentsList/austin.html", {'distance_result': Austin_List})