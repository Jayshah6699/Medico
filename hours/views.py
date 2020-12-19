from django.shortcuts import render

def index(request):
    return render(request, 'hours/index.html')

def intern(request):
    return render(request, 'hours/intern.html')

def doctor(request):
    return render(request, 'hours/doctor.html')

def message(request):
    return render(request, 'hours/message.html')

def calendar(request):
    return render(request, 'hours/calendar.html')
