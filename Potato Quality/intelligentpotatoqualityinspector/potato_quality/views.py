# from django.shortcuts import render
# Create your views here.
# urlpatterns = [
#    path('', views.index, name='index'),
#]

# New changes here(Static web page)

# from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
#    text="Hello and welcome to my first application"
#    return HttpResponse(text)

# New changes here(Dynamic web page)

from django.shortcuts import render
from django.http import HttpResponse
import datetime
def index(request):
    now=datetime.datetime.now()
    text="<marquee><h1>Hello and welcome to my first application: : %s</h1></marquee>" %now
    return HttpResponse(text)
