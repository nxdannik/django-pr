from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('payment/', views.payment, name='payment'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]