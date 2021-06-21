from django.shortcuts import render
from .forms import FirstMeeting

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def programs(request):
    return render(request, 'programs.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def firstMeeting(request):
    form = FirstMeeting
    return render(request, 'first_meeting.html', {'form':form})