from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import TripTemplate

# Create your views here.

def listing(request):

    thetrips = TripTemplate.objects.all()
    context = {
        'thetrips': thetrips
    }

    return render(request, 'trips/listing.html', context)

def trip(request, trip_id):

    trip = get_object_or_404(TripTemplate,pk=trip_id)

    context = {
        'trip':trip
    }


    thetrip = TripTemplate.objects.get(id=trip_id)

    context = {'thetrip':thetrip}

    return render(request, "trips/trip.html", context)