from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse('Home Page')

def Rooms(request):
    return HttpResponse('Rooms')

class Test():
    def render_test(request):
        return HttpResponse('Test')
