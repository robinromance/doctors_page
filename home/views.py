from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import BookingForm
from . models import Departments, Doctors 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form= BookingForm()
    dict_form= {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctors(request):
    dect_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dect_docs)

def contact(request):
    return render(request, 'contact.html')

def departments(request):
    dect_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'departments.html', dect_dept)

