from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages




def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST.get('name')
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made a inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id = user_id)
            if has_contacted:
               messages.warning(request,'You already submit a request in this property')
               return redirect('../listings/'+listing_id)

        contact = Contact(listing = listing,listing_id= listing_id,name=name,email=email,
        phone = phone,message = message,user_id= user_id)
        contact.save()
        messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
        return redirect('../listings/'+listing_id)