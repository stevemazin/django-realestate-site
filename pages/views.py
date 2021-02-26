from django.shortcuts import render

from listings.choices import price_choices, bedroom_choices, locality_choices, agreement_choices
# Import Models
from listings.models import Listing
from realtors.models import Realtor

def index (request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'locality_choices': locality_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'agreement_choices': agreement_choices
    }
    return render(request, 'pages/index.html', context)

def about (request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    # print(request.path)
    return render(request, 'pages/about.html', context)
