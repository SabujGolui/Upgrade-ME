from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Feedback
from django.contrib import messages

# Create your views here.

def index(requests):
    return render(requests, 'index.html')

def about(requests):
    return render(requests, 'about.html')

def paid_courses(requests):
    return render(requests, 'paid_courses.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        feedback = Feedback(name=name,email=email,phone=phone, desc=desc,date=datetime.today())
        feedback.save()
        messages.success(request, 'Your feedback has been sent!!')
    return render(request, 'feedback.html')