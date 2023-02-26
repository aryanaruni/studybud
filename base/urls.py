from django.urls import path

from .views import (
    Home,
    Rooms,
    Test,
)

urlpatterns = [
    path('', Home),
    path('rooms/', Rooms),
    path('test/', Test.render_test),
]
