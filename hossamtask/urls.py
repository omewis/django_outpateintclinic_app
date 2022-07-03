"""hossamtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookingapp.views import retrievebooking
from bookingapp.views import addnewbooking,buiinfo,retrievedoctor,Buildings,cliinfo,Clinics,docinfo,index,listallbooking,makeV,mess,note,Overview,allbooking,addnewdoctor,addnewclinic,ADDnewclinic,addnewbuilding


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookingall', retrievebooking,name='list_all_booking'),
    path('newbooking', addnewbooking, name='add_new_booking'),
    path("buiinfo.html", buiinfo, name='buiinfo'),
    path('Buildings.html', Buildings, name='Buildings'),
    path('cliinfo.html', cliinfo, name='cliinfo'),
    path('Clinics.html', Clinics, name='Clinics'),
    path('docinfo.html', docinfo, name='docinfo'),
    path('Doctors.html', retrievedoctor, name='Doctors'),
    path('index.html', index, name='index'),
    path('listallbooking.html', listallbooking, name='listallbooking'),
    path('makeV.html', makeV, name='makeV'),  
    path('mess.html',mess, name='mess.html'),    
    path('note.html', note, name='note'),     
    path('Overview.html', Overview, name='Overview'),
    path('allbooking.html', allbooking, name='list_all_booking'), 
    path('adddoctor.html',addnewdoctor , name='add_doctor'),
    path('addclinic.html',addnewclinic , name='add_clinic'),
    path('newclinic.html',ADDnewclinic , name='new_clinic'),
    path('addbuilding.html',addnewbuilding , name='add_building'), 
    
]
