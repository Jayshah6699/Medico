from django.shortcuts import render

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

def _menu(request, message, label_links):
    context = {
        'message': message,
        'label_links': label_links
    }
    
    return render(request, 'hours/_menu.html', context)

def intern(request):
    return render(request, 'hours/intern.html')

def doctor(request):
    return render(request, 'hours/doctor.html')

def message(request):
    return render(request, 'hours/message.html')

def calendar(request):
    return render(request, 'hours/calendar.html')


