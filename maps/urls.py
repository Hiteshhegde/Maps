from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_destination, name='get-destination'),
]