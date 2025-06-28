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
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/order/', views.create_order, name='create_order'),
    path('order/success/', views.order_success, name='order_success'),
]