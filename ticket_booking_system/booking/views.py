from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Ticket
from .forms import TicketForm

def index(request):
    events = Event.objects.all()
    return render(request, 'booking/index.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'booking/event_detail.html', {'event': event})

def book_ticket(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            buyer_name = form.cleaned_data['buyer_name']
            quantity = form.cleaned_data['quantity']
            ticket = Ticket(event=event, buyer_name=buyer_name, quantity=quantity)
            ticket.save()
            return redirect('booking_success')  # Redirect to a success page or home page
    else:
        form = TicketForm()
    
    return render(request, 'booking/book_ticket.html', {'form': form, 'event': event})

def booking_success(request):
    return render(request, 'booking/booking_success.html')