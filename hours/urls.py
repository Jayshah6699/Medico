from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('intern', views.intern, name='intern'),
    path('doctor', views.doctor, name='doctor'),
    path('message', views.message, name='message')
]