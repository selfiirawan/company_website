from django.shortcuts import render, redirect
from app.models import (
    GeneralInfo, 
    Service, 
    Testimonial, 
    FrequentlyAskedQuestion,
)
from datetime import datetime

# Create your views here.
def index(request):
    general_info = GeneralInfo.objects.first()

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()

    context = {
        "company_name": general_info.company_name,
        "location": general_info.location,
        "phone": general_info.phone, 
        "email": general_info.email,
        "open_hours": general_info.open_hours,
        "video_url": general_info.video_url,
        "twitter_url": general_info.twitter_url,
        "facebook_url": general_info.facebook_url,
        "instagram_url": general_info.instagram_url,
        "linkedin_url": general_info.linkedin_url,

        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
    }

    return render(request, "index.html", context)


def contact_form(request):
    
    if request.method == "POST":
        print("\nContact form submitted\n")
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
    
    return redirect('home')