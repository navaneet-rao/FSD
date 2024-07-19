from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking
from .forms import BookingForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'booking/event_list.html', {'events': events})

def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.user = request.user
            booking.save()
            return redirect('my_bookings')  # Redirect to a page showing user's bookings
    else:
        form = BookingForm()

    return render(request, 'booking/book_ticket.html', {'form': form, 'event': event})

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

