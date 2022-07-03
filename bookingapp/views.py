from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Booking, clinic, doctor ,clininfo,num_of_building

def retrievebooking(request):
    x = Booking.objects.all()

    return render(request ,'bookingapp/listallbooking.html',{'Booking':x})
from django.shortcuts import redirect
from .forms import BookingForm , DoctorForm ,clinicForm ,cliccForm ,buildingForm

def addnewbooking(request):
    form = BookingForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_booking')

    return render(request, 'bookingapp/makeV.html',{'form':form})

def addnewdoctor(request):
    form = DoctorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Doctors')

    return render(request, 'bookingapp/adddoctor.html',{'form':form})

def addnewclinic(request):
    form = cliccForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Clinics')

    return render(request, 'bookingapp/addclinic.html',{'form':form})

def ADDnewclinic(request):
    form = clinicForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Clinics')

    return render(request, 'bookingapp/newclinic.html',{'form':form})

def addnewbuilding(request):
    form = buildingForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Buildings')

    return render(request, 'bookingapp/addbuilding.html',{'form':form})

def cliinfo(request):
    dept = clininfo.objects.all()
    return render(request, 'bookingapp/cliinfo.html', {'clinic':dept})  

   

def retrievedoctor(request):
    x = doctor.objects.all()

    return render(request ,'bookingapp/Doctors.html',{'doctors':x})


def buiinfo(request):
    return render(request, 'bookingapp/buiinfo.html', {})

def Buildings(request):
     x = num_of_building.objects.all()
     return render(request, 'bookingapp/Buildings.html', {'building':x})


def Clinics(request):

    x = clinic.objects.all()
    return render(request, 'bookingapp/Clinics.html', {'clinic':x})                 

def docinfo(request):
    return render(request, 'bookingapp/docinfo.html', {})                 

                

def index(request):
    return render(request, 'bookingapp/index.html', {})                 

def listallbooking(request):
    return render(request, 'bookingapp/listallbooking.html', {})                 

def makeV(request):
    form = BookingForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_booking')

    return render(request, 'bookingapp/makeV.html',{'form':form})
 

def mess(request):
    return render(request, 'bookingapp/mess.html', {})   

def note(request):
    return render(request, 'bookingapp/note.html', {})   

def Overview(request):
    return render(request, 'bookingapp/Overview.html', {})   

def allbooking(request):
     x = Booking.objects.all()

     return render(request ,'bookingapp/listallbooking.html',{'Booking':x})


