# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define the root URL pattern with the name 'index'
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/book/', views.book_ticket, name='book_ticket'),
    path('booking/success/', views.booking_success, name='booking_success'),
    # Add other URL patterns as needed
]
