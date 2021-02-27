from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('inquiries/<int:listing_id>', views.inquiry_form, name='inquiry'),
    path('contact/<int:listing_id>', views.contact, name='contact'),
]