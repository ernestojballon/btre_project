from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives



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
        # we want the email to be sent only if the contact form was submitted
        # First way with the send_mail method
        ##################################################################
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + ' '+ 
        #     request.get_full_path()
        #       + ' .Sign into the admin panel for more info ',
        #     'ernestoballono@gmail.com',
        #     [realtor_email,'ernestoballono@gmail.com'],
        #     fail_silently=False
        # )
        ###############################################################
        # Second way with the EmailMultiAlternatives method 
        # subject, from_email, to = 'site Registration', 'support@site.com', 'ernestoballono@gmail.com'
        # text_content = 'Click on link to finish registration'
        # html_content = '<html><body><a href="http://127.0.0.1:8000/listings/' + listing_id +'">Click Here</a></body></html>'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()



        messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
        return redirect('../listings/'+listing_id)