
from django.shortcuts import render, redirect
from .models import Review

def home(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/home.html', {'reviews': reviews})

def add_review(request):
    if request.method == "POST":
        name = request.POST['name']
        review_text = request.POST['review']
        Review.objects.create(name=name, review_text=review_text)
        return redirect('/')
    return redirect('/')
