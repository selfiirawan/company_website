from django.shortcuts import render
from app.models import GeneralInfo, Service, Testimonial, FrequencyAskedQuestion
from datetime import datetime

# Create your views here.
def index(request):
    general_info = GeneralInfo.objects.first()

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequencyAskedQuestion.objects.all()

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

# def aboutus(request):
#     context = {}
#     return render(request, 'aboutus.html', context)