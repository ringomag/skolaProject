from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def programs(request):
    return render(request, 'programs.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def firstMeeting(request):
    return render(request, 'first_meeting.html', {})