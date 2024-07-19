from django.urls import path
from .views import event_list, book_ticket, my_bookings

urlpatterns = [
    path('', event_list, name='event_list'),
    path('book/<int:event_id>/', book_ticket, name='book_ticket'),
    path('my_bookings/', my_bookings, name='my_bookings'),
]

