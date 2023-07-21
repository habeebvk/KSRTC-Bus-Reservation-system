from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
from . views import(
    SeatBookingView
)

urlpatterns=[
    path('hii',views.index,name='index'),
    path('cer',views.cer,name='cer'),
    path('certificate1',views.cer1,name='cert1'),
    path('certificate2',views.cer2,name='cert2'),
    path('certificate3',views.cer3,name='cert3'),
    path('certificate4',views.cer4,name='cert4'),
    path('certificate5',views.cer5,name='cert5'),
    path('certificate6',views.cer6,name='cert6'),
    path('certificate7',views.cer7,name='cert7'),
    path('certificate8',views.cer8,name='cert8'),
    path('certificate/<int:pk>',views.certi,name='cert'),
    path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('book-now/<str:id>',views.book_now,name='book-now'),
    path('cancel-room/<str:id>',views.cancel_room,name='cancel-room'),
    path('delete-room/<str:id>',views.delete_room,name='delete-room'),
    path('confirm-now-booking',views.book_confirm,name="book_confirm"),
    



    path('',views.indexa, name='u_homepage'),
    # path('category/<slug:val>', views.PackageView.as_view(), name='package'),
    # path('place-title/<val>', views.PackagePlace.as_view(), name='place-title'),
    path('packages/',views.package, name='package'),
    path('aboutus/',views.about, name='aboutus'),
    path('contactus/',views.contact, name='contactus'),
    path('mytrip/',views.mytrip, name='mytrips'),
    # path('register/',views.register, name='register'),
    # path('registero/',views.registerorg, name='registerorg'),
    path('blanket/',views.blanket, name='blanket'),
    path('casamontana/',views.casamontana, name='casamontana'),
    path('coorg/',views.coorg, name='coorg'),
    path('fortkochi/',views.fort, name='fortkochi'),
    path('fragrantnature/',views.fragrant, name='fragrantnature'),
    path('grandplaza/',views.grand, name='grandplaza'),
    path('guestdetails/',views.guest, name='guestdetails'),
    path('hotls/<slug:val>',views.ViewHot, name='hotels'),
    path('personaldetails/<slug:val>',views.person, name='personaldetails'),
    path('isaacresidency/',views.isaac, name='isaacresidency'),
    path('kodaikanal/',views.kodaikanal, name='kodaikanal'),
    path('kurinjiwanderlust/',views.kurinji, name='kurinjiwanderlust'),
    path('lecelestium/',views.le, name='lecelestium'),
    path('login/',auth_views.LoginView.as_view(template_name='login1.html'),name='login'),
    path('logs/',views.log, name='logs'),
    path('munnar/',views.munnar, name='munnar'),

    path('mysore/',views.mysore, name='mysore'),

    path('detail/<slug:val>',views.rout_dt, name='city_detail'),

    path('notifications/',views.notifications, name='notifications'),
    path('ooty/',views.ooty, name='ooty'),
    path('panoramicgateway/',views.panorama, name='panoramicgateway'),
    path('payment/',views.payment, name='payment'),
    path('room1/',views.room1, name='room1'),
    path('room2/',views.room2, name='room2'),
    path('room3/',views.room3, name='room3'),
    path('room4/',views.room4, name='room4'),
    path('room5/',views.room5, name='room5'),
    path('room6/',views.room6, name='room6'),
    path('room7/',views.room7, name='room7'),
    path('roomdetails/',views.roomdtls, name='roomdetails'),
    path('roompayment/',views.roompayment, name='roompayment'),
    path('rooms/',views.rooms, name='rooms'),
    path('seatbooking/<str:firstname>',SeatBookingView.as_view(), name='seatbooking'),
    path('ticket/',views.ticket, name='ticket'),
    path('wayanad/',views.wayanad, name='wayanad'),

]