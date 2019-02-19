from django.urls import path
from . import views

app_name = 'PCfix'
urlpatterns = [
    path('uploadPic/',views.receiveImage),
    path('login/',views.login),
    path('enroll/',views.enroll),
    path('userAlter/',views.userAlter),
    path('newOrder/',views.newOrder),
    path('orders/',views.orders),
    #path('orders2/',views.orders2),
    path('order/<str:no>/',views.order),
    path('annul/',views.annul),
    path('repair/',views.repair),
    path('receive/',views.receive),
    path('complete/',views.complete),
    path('repairInfo/',views.repairInfo),
    path('check/',views.check)
]