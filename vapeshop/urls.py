from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # ← це обов'язково!
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]
from django.contrib import admin
from django.urls import path, include  # додай include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # підключаємо urls додатку store
]
