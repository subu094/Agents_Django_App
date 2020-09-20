from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('ny/',views.nyList),
    path('bt/',views.btList),
    path('la/',views.laList),
    path('cc/',views.ccList),
    path('ht/',views.htList),
    path('px/',views.pxList),
    path('sd/',views.sdList),
    path('ds/',views.dsList),
    path('sj/',views.sjList),
    path('at/',views.atList),
    path('cs/',views.csList)
]
