from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save feedback to database
            Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            print("Thank You for submitting feedback")
            return redirect('/#contact')  # redirect to a thank-you page
    else:
        form = FeedbackForm()
        print(messages.error)
    return render(request, '/#contact', {'form': form})