from django.shortcuts import render

def index(request):
    return render(request, 'hours/index.html')

def intern(request):
    return render(request, 'hours/intern.html')

def doctor(request):
    return render(request, 'hours/doctor.html')
