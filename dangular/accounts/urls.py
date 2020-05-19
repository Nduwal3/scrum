from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # '/register/'
    path('register', views.register, name='register')
]
