from django.urls import path
from .views import home

app_name = 'inicio'

urlpatterns = [
    path('', home, name='home'),
]
