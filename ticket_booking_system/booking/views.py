from django.shortcuts import render, get_object_or_404
from .models import Event, Ticket

def index(request):
    events = Event.objects.all()
    return render(request, 'booking/index.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'booking/event_detail.html', {'event': event})
