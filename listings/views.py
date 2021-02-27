from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from users.models import Inquiry
from .choices import price_choices, bedroom_choices, locality_choices, agreement_choices
from users.forms import UserEnquiryForm
from django.contrib import messages


def index (request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    print(f'Paginator numPages: {paginator.num_pages}')
    print(f'Paginator objects: {paginator.count}')
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing (request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    form = UserEnquiryForm()

    context = {
        'listing': listing,
        'form': form
    }
    return render(request, 'listings/listing.html', context)


def search (request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Agreement Terms
    if 'agreement_terms' in request.GET:
        agreement_terms = request.GET['agreement_terms']
        if agreement_terms == 'rent':
            print('Show Rentals')
            queryset_list = queryset_list.filter(rental=True)
        elif agreement_terms == 'buy':
            print('Show For Sale')
            queryset_list = queryset_list.filter(for_sale=True)
        elif agreement_terms == 'purchasable':
            queryset_list = queryset_list.filter(for_sale=True, rental=True)
    

    # Locality
    if 'locality' in request.GET:
        locality = request.GET['locality']
        if locality:
            print(locality)
            queryset_list = queryset_list.filter(locality__iexact=locality)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # lte -less than or equal to
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # lte -less than or equal to
            queryset_list = queryset_list.filter(price__lte=price)


    # Paginations
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    

    context = {
        'locality_choices': locality_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'agreement_choices': agreement_choices,
        'listings': paged_listings,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


def inquiry_form (request, listing_id):
    form = UserEnquiryForm()
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {'form': form, 'listing': listing}
    return render(request, 'listings/_inquiry.html', context)


def contact(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == 'POST':
        form = UserEnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            print(f'This is the username: {name}') 
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            listing_id = listing_id
            listing = listing
            print(f'This is the listing {listing}')
            user_id = request.POST['user_id']
            realtor_email = listing.realtor.email

            # Test to see if there exists a similar listing inquiry in the DB
            phone = form.cleaned_data.get('phone')
            inquiryObj = Inquiry.objects.filter(listing=listing, phone=phone, name=name, email=email).exists()

            if inquiryObj == True:
                print('An enquiry exists')
                messages.warning(request, "Looks like you recently made an inquiry on this property...We'll get back to you soon!")
                
                return redirect(f'http://127.0.0.1:8000/listings/{listing_id}')

            # Everything is good => Save to the DB
            inquiry = Inquiry(
                listing=listing, listing_id=listing_id,
                email=email, name=name, phone=phone,
                message=message, user_id=user_id)

            inquiry.save()
            messages.success(request, f'Enquiry sent successfully!')
            return redirect(f'http://127.0.0.1:8000/listings/{listing_id}')

        
    else:
        form = UserEnquiryForm()

    context = {'form':form, 'listing': listing}
    return render(request, 'listings/_inquiry.html', context)
