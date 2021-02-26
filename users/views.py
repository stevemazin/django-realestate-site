from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from listings.models import Listing
from .models import Inquiry
from .forms import UserEnquiryForm

def dashboard(request, user_id):
    inquiries = Inquiry.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    context = {
        'contacts': inquiries,
    }
    return render(request, 'users/dashboard.html', context)
