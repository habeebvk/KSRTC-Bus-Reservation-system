from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Buses, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'buses/home.html')
    else:
        return render(request, 'buses/signin.html')
    
# def indexa(request):
#     if request.user.is_authenticated:
#         return render(request, 'booking/ksrtctour.html')
#     else:
#         return render(request, 'buses/signin.html')


@login_required(login_url='signin')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Buses.objects.filter(source1=source_r, dest1=dest_r, date1=date_r)
        if bus_list:
            return render(request, 'buses/list.html', locals())
        else:
            context["error"] = "Sorry no buses available"
            return render(request, 'buses/findbus.html', context)
    else:
        return render(request, 'buses/findbus.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Buses.objects.get(id=id_r)
        if bus:
            if bus.rem1 > int(seats_r):
                name_r = bus.bus_name1
                cost = int(seats_r) * bus.price1
                source_r = bus.source1
                dest_r = bus.dest1
                nos_r = Decimal(bus.nos1)
                price_r = bus.price1
                date_r = bus.date1
                time_r = bus.time1
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem1 - seats_r
                Buses.objects.filter(id=id_r).update(rem1=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'buses/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'buses/findbus.html', context)

    else:
        return render(request, 'buses/findbus.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Buses.objects.get(id=book.busid)
            rem_r = bus.rem1 + book.nos
            Buses.objects.filter(id=book.busid).update(rem1=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'buses/error.html', context)
    else:
        return render(request, 'buses/findbus.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'buses/booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'buses/findbus.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'buses/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'buses/signup.html', context)
    else:
        return render(request, 'buses/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'buses/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'buses/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'buses/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'buses/signin.html', context)

def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'buses/success.html', context)

def pay1(request):
    return render(request, 'buses/pay1.html')    
