from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Contact
from .models import Rooms,Booking
from login.models import Customer
from django.contrib import messages
from django.http import HttpResponse
import datetime
def index(request):
    return render(request,'booking/index.html',{})
def contact(request):
    if request.method=="GET":
     return render(request,"contact/contact.html",{})
    else:
     username=request.POST['name']
     email=request.POST['email']
     message=request.POST['message']
     data=Contact(name=username,email=email,message=message)
     data.save()
     return render(request,"contact/contact.html",{'message':'Thank you for contacting us.'})
def book(request):
    if request.method=="POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        request.session['start_date']=start_date
        request.session['end_date']=end_date
        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        no_of_days=(end_date-start_date).days
        data=Rooms.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date)
        request.session['no_of_days']=no_of_days
        return render(request,'booking/book.html',{'data':data})
    else:
        return redirect('index')
def book_now(request,id):
    if request.session.get("username",None) and request.session.get("type",None)=='customer':
        if request.session.get("no_of_days",1):
            no_of_days=request.session['no_of_days']
            start_date=request.session['start_date']
            end_date=request.session['end_date']
            request.session['room_no']=id
            data=Rooms.objects.get(room_no=id)
            bill=data.price*int(no_of_days)
            request.session['bill']=bill
            roomManager=data.manager.username
            return render(request,"booking/book-now.html",{"no_of_days":no_of_days,"room_no":id,"data":data,"bill":bill,"roomManager":roomManager,"start":start_date,"end":end_date})
        else:
            return redirect("index")
    else:
        next="book-now/"+id
        return redirect('user_login')
def book_confirm(request):
    room_no=request.session['room_no']
    start_date=request.session['start_date']
    end_date=request.session['end_date']
    username=request.session['username']
    user_id=Customer.objects.get(username=username)
    room=Rooms.objects.get(room_no=room_no)
    amount=request.session['bill']
    start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
    end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
    data=Booking(room_no=room,start_day=start_date,end_day=end_date,amount=amount,user_id=user_id)
    data.save()
    room.is_available=False
    room.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    del request.session['room_no']
    messages.info(request,"Room has been successfully booked")
    return redirect('user_dashboard')
def cancel_room(request,id):
    data=Booking.objects.get(id=id)
    room=data.room_no
    room.is_available=True
    room.save()
    data.delete()
    return HttpResponse("Booking Cancelled Successfully")
def delete_room(request,id):
    data=Rooms.objects.get(id=id)
    manager=data.manager.username
    if manager==request.session['username']:
        data.delete()
        return HttpResponse("You have deleted the room successfully")
    else:
        return HttpResponse("Invalid Request")


            



    
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from .models import Destination, Dest,PersonalDetail, Hotels,Notifi, certificate
from.forms import feedbackForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def indexa(request):
    root1=Dest.objects.all()
    return render(request, "booking/ksrtctour.html",locals())

def cer(request):
     return render(request,"booking/cer.html")

def cer1(request):
    return render(request,"booking/Certificate1.html")

def cer2(request):
    return render(request,"booking/Certificate2.html")

def cer3(request):
    return render(request,"booking/Certificate3.html")

def cer4(request):
    return render(request,"booking/Certificate4.html")

def cer5(request):
    return render(request,"booking/Certificate5.html")

def cer6(request):
    return render(request,"booking/Certificate6.html")

def cer7(request):
    return render(request,"booking/Certificate7.html")

def cer8(request):
    return render(request,"booking/Certificate8.html")

def package(request):
   dict_city={
        'city':Destination.objects.all()
    }
   return render(request, "booking/packages.html", dict_city)


# class PackageView(View):
#     def get(self,request,val):
#         dest=Destination.objects.filter(category=val)
#         place=Destination.objects.filter(category=val).values('name')
#         return render(request, 'packages.html', locals())

# class PackagePlace(View):
#     def get(self,request,val):
#         dest=Destination.objects.filter(category=val)
#         place=Destination.objects.filter(category=dest[0].category).values('name')
#         return render(request, 'packages.html', locals())

# class PackageDetail(View):
#     def get(self, request, pk):
#         destinations=Destination.objects.get(pk=pk)
#         return render(request, 'Package_detail.html', locals())

        

def about(request):
    return render(request, 'booking/aboutus.html')

def contact(request):
    return render(request, 'booking/contact.html')

# def mytrip(request,val):
#     bus = Bus.objects.filter(desti = val)
#     return render(request, 'mytrip.html',locals())

def mytrip(request,val):
    # root=Dest.objects.filter(city = val)
    return render(request, 'mytrip.html', locals())    

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been created. You can log in now!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     context = {'form': form}
#     return render(request, 'Register.html', context)

def blanket(request):
    return render(request, 'Blankethotel.html')
# def registerorg(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Your account has been created. You can log in now!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     context = {'form': form}
#     return render(request,'Register.html',context)
def casamontana(request):
    return render(request, 'casamontana.html')

def coorg(request):
    return render(request, 'coorg.html')

def fort(request):
    return render(request, 'fortkochi.html')

def fragrant(request):
    return render(request, 'fragrantnature.html')

def grand(request):
    return render(request, 'grandplaza.html')

def guest(request):
    return render(request, 'guestdetails.html')

def ViewHot(request,val):
    city=Hotels.objects.all()    
    root=Dest.objects.filter(city = val)
    return render(request, "booking/hotels.html", locals())

def certi(request,pk):
    cer=certificate.objects.filter(pk=pk)
    return render(request, "booking/certificate.html", locals())

def person(request,val):
    # if request.method == 'POST':
    #     form = PersonalDetailForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, f'Personal details are updated successfully')
    #         root=Dest.objects.filter(city = val)
    #         return render(request,'seatbk.html', locals())
    # else:
    #     form = PersonalDetailForm()        
    return render(request, 'personaldetails.html')

def isaac(request):
    return render(request, 'isaacsresidency.html')

def kodaikanal(request):
    return render(request, 'kodaikanal.html')

def kurinji(request):
    return render(request, 'kurinjiwanderlust.html')

def le(request):
    return render(request, 'lecelestium.html')
    
def  login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username, password=password)
             if user is not None:
                messages.info(request,f"You are now logged in as {username}")
                return redirect("homepage")
             else:
                 messages.error(request,'Username or password is incorrect')
        else:
            messages.error(request,'Username or password is incorrect')
    form = AuthenticationForm()
    return render(request=request,template_name="login1.html",context={"form":form})

def log(request):
    return render(request, 'Login.html')

def munnar(request):
    return render(request, 'munnar.html')

def mysore(request):
    return render(request, 'mysore.html')
    
def rout_dt(request,val):
    root=Dest.objects.filter(city = val)
    return render(request, "booking/nelliyampathy.html",locals())

def notifications(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form2.cleaned_data.get('user')
            messages.success(request, f'Your feedback are recorded successfully')
            # noti=Notifi.objects.all()
            return redirect('/', locals())
    else:
        form = feedbackForm()
    return render(request, 'booking/notifications.html', {'form':form})

def ooty(request):
    return render(request, 'ooty.html')

def panorama(request):
    return render(request, 'panoramicgateway.html')

def payment(request):
    return render(request, 'payment.html')

def room1(request):
    return render(request, 'room1.html')

def room2(request):
    return render(request, 'room2.html')

def room3(request):
    return render(request, 'room3.html')

def room4(request):
    return render(request, 'room4.html')

def room5(request):
    return render(request, 'room5.html')

def room6(request):
    return render(request, 'room6.html')

def room7(request):
    return render(request, 'room7.html')

def room8(request):
    return render(request, 'room8.html')

def roomdtls(request):
    return render(request, 'roomdtls.html')

def roompayment(request):
    return render(request, 'roompayment.html')

def rooms(request):
    return render(request, 'rooms.html')

# def seatbooking(request,val):
#     detail=PersonalDetail.objects.filter(firstname=val)
#     return render(request, 'seatbk.html',locals())


class SeatBookingView(ListView):
    model = PersonalDetail
    template_name = 'seatbk.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'Total'
    

    def get_queryset(self):
        user = get_object_or_404(PersonalDetail, firstname=self.kwargs.get('firstname'))
        return PersonalDetail.objects.filter(firstname=user)    

def ticket(request):
    return render(request, 'ticket.html')

def wayanad(request):
    return render(request, 'wayanad.html')


def indexi(request):
    return render(request,'home1.html')
# def book(request):
#     return render(request,'booking.html')
def allr(request):
    return render(request,'allroom.html')
def addr(request):
    return render(request,'addroom.html')   
def add(request):
    return render(request,'add.html')     
def log(request):
    return render(request,'manager1.html')
def reg(request):
    return render(request,'manager2.html')
def hotel(request):
    return render(request,'manager3.html')    

