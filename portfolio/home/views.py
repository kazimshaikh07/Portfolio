from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                message=message_text,
                date=datetime.today().date(),
            )
            contact.save()
            messages.success(request, "Thank you for reaching out! Your message has been sent successfully. I’ll get back to you as soon as possible.")
            return redirect('home')  # Post/Redirect/Get to avoid resubmission
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, "index.html")