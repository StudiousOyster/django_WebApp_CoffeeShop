from django.shortcuts import render
from django.http import HttpResponse
from .models import coffee_db

# Create your views here.
def home(request):
    coffee = coffee_db.objects.all()  # Fetch all coffee items from the database
    return render(request, 'home.html', {'coffee': coffee})