from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "course_title": "Django Course",
        "current_date": datetime.now(),
        "user": {
            "name": "John Doe",
            "email": "john.doe@example.com",
        },
        "price": 199.9999,
        "text": "Welcome to the Django Course!"
    }
    return render(request, "index.html", context)