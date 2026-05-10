from django.urls import path
from .import views

urlpatterns = [
    path('projectapi/', views.projectApi, name='projectapi'),
    path('serviceapi/', views.serviceApi, name='serviceapi'),
    path('sendEmail/', views.send_email, name='sendEmail'),
]
