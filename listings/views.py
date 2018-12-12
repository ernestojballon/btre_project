from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from listings.choices import price_choices, bedroom_choices,states_choices

def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }

    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk = listing_id)
    context = {
        'listing': listing
    }


    return render(request,'listings/listing.html',context)

def search(request):
    # create a variable and asigned the object from the database
    
    paged_queryset_listing = Listing.objects.order_by('-list_date')
    # 
    
    
    # filter for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            paged_queryset_listing = paged_queryset_listing.filter(description__icontains = keywords)
    # we use icontains if we want to find any match inside the field 

    # filter for city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            paged_queryset_listing = paged_queryset_listing.filter(city__iexact = city)
        # we use iexact to match the field with the parameter but is not case sensitive if
        # we want case casensitive we would use just exact    
   
    # filter for state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # option 1
             paged_queryset_listing = paged_queryset_listing.filter(state__iexact = state)
            # option 2  the next line does the same as the previous one  
            # paged_queryset_listing = paged_queryset_listing.extra(where = ["state like %s"],params = [state])
    
    # filter for bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            paged_queryset_listing = paged_queryset_listing.filter(bedrooms__gte = bedrooms)
    # filter for bedrooms
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            paged_queryset_listing = paged_queryset_listing.filter(price__lte = price)

    # page = request.GET.get('page')
    # paginator = Paginator(paged_queryset_listing,3)
    # paged_queryset_listing = paginator.get_page(page)
    # with the next line we just sorted the dictionary 
    bedroom_choices_sorted = sorted(bedroom_choices.items(),key = lambda x : x[1])
    states_choices_sorted = sorted(states_choices.items(),key = lambda x : x[1])
    price_choices_sorted = sorted(price_choices.items(),key = lambda x : x[0])

    context = {
        'listings':paged_queryset_listing,
        'states_choices': states_choices_sorted,
        'price_choices' :price_choices_sorted,
        'bedroom_choices': bedroom_choices_sorted,
        'values': request.GET
    } 

    return render(request,'listings/search.html', context)

    
