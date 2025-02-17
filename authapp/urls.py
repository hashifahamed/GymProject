from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="login"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll, name="enroll"),
    path('about',views.about, name="about"),
    path('services',views.services, name="services"),
    path('attendance',views.attendance, name="attendance"),
    path('trainer',views.trainer, name="trainer"),
    
    
    
]
