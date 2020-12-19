from django.shortcuts import render, redirect

from .forms import DepartmentForm
from .models import Department

def index(request):
    message = "Please select if you are a doctor, volunteer, or would like to see the calendar."
    label_links = (
        ("I'm a doctor", 'doctor'),
        ("I'm an intern", 'intern'),
        ("See calendar", 'calendar')
    ) 

    return _menu(request, message, label_links)

def departments(request):
    message = "Please select which department you would like to view the calendar for."
    label_links = (
        ('Emergency Room', 'index'),
        ('Operating Room', 'index'),
        ('Acute Care Unit', 'index')
    )

    return _menu(request, message, label_links)

def message(request):
    message = "Congrats! You have scheduled a 6:00AM shift at the Operating Room on 12/22/20"
    label_links = (
        ('Back to home', 'index'),
    )

    return _menu(request, message, label_links)

def _menu(request, message, label_links):
    context = {
        'message': message,
        'label_links': label_links
    }
    
    return render(request, 'hours/_menu.html', context)

def intern(request):
    return render(request, 'hours/intern.html')

def doctor(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        
        if form.is_valid():
            Department.objects.create(
                name=form.cleaned_data['name']
            )

            return redirect('doctor')
    
    else:
        form = DepartmentForm()

    return render(request, 'hours/doctor.html', {'form': form})

def calendar(request):
    return render(request, 'hours/calendar.html')


