from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')

def contacts(request):
    return render(request, 'store/contacts.html')

def delivery(request):
    return render(request, 'store/delivery.html')

def payment(request):
    return render(request, 'store/payment.html')