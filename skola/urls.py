from django.urls import path
from . import views
from .views import FirstMeetingView, BlogPostView

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('programs/', views.programs, name="programs"),
    path('first_meeting/', FirstMeetingView.as_view(), name="first_meeting"),
    path('blog/', views.blog, name="blog"),
    path('addPost/', BlogPostView.as_view(), name="addPost"),
    path('BlogDetails/<str:pk>', views.BlogDetails, name="details"),
    
]