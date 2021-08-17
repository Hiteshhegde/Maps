from django.shortcuts import render, get_object_or_404
from geopy import point
from .forms import DistanceModelForm
from .models import Distance
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils  import get_geo, get_center_coordinates, get_zoom
import folium 

# Create your views here.
def get_destination(request):

    destination = None
    distance = None
    form = DistanceModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='distance')

    #ip locator 
    ip = '35.241.19.142'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)

    #location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    #intital folium app
    m = folium.Map(width=800, height= 500, location=get_center_coordinates(l_lat,l_lon), zoom_start=8)    
    
    tooltip = "Click me!"
    popupA = pointA
    

    #if form is valid create a save instance of the form
    if form.is_valid():

        #Creating instance of form save
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        
        #destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        popupB = pointB
        #distance measure between A and B
        distance = round(geodesic(pointA, pointB).km, 2)
        
        m = folium.Map(width=800, height= 500, location=get_center_coordinates(l_lat,l_lon,d_lat, d_lon), zoom_start=get_zoom(distance))
        
        #folium map modification
        folium.Marker(
            location=pointA, 
            popup=popupA,
            icon=folium.Icon(color="green"), 
            tooltip=tooltip
        ).add_to(m)
        folium.Marker(
            location=pointB, 
            popup=popupB,
            icon=folium.Icon(color="red"), 
            tooltip=tooltip
        ).add_to(m)

        #draw the line 
        line = folium.PolyLine(locations=[pointA, pointB], weight=1, color='blue')
        m.add_child(line)

        #saving the instance of form with user updated values 
        instance.destination = destination
        instance.location = location
        instance.distance = distance
        instance.save()

    #obj = get_object_or_404(Distance, id=1)


    context = {
        'form' : form,
        'location':city['city'],
        'destination': destination,
        'distance' : distance,
        'map': m._repr_html_()
    }

    template_name = 'maps/index.html'
    return render(request, template_name, context)

