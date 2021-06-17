from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('programs/', views.programs, name="programs"),
    path('first_meeting', views.firstMeeting, name="first_meeting"),
    path('blog/', views.blog, name="blog"),
    
]