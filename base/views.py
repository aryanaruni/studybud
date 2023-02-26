from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    # return HttpResponse('Home Page')
    return render(request , 'home.html')

def Rooms(request):
    # return HttpResponse('Rooms')
    return render(request , 'rooms.html')

class Test():
    def render_test(request):
        return HttpResponse('Test')
        # return render(request , 'home.html')
