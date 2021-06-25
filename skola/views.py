from django.shortcuts import render, redirect
from .forms import FirstMeetingForm, BlogForm
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from .models import Blog
#import pagination
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def programs(request):
    return render(request, 'programs.html', {})

def blog(request):
    blogPosts = Blog.objects.all()

    #paginator
    p = Paginator(Blog.objects.all(), 2)
    page = request.GET.get('page')
    posts = p.get_page(page)


    return render(request, 'blog.html', {'blogPosts':blogPosts, 'posts':posts})

class FirstMeetingView(View):
    form = FirstMeetingForm

    def get(self, request, *args, **kwargs):
        form = FirstMeetingForm
        return render(request, 'first_meeting.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = FirstMeetingForm
        form = FirstMeetingForm(request.POST)
       
        if form.is_valid():
            print("neki tekst")

            message_name = "ime i prezime: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name']
            message_content = "Zakazivanje inicijalnog termina"
            message_from = request.POST['email']
            message_first_name = form.cleaned_data['first_name']
            print(message_first_name)

            send_mail(
            message_name, #subject
            message_content, #message
            message_from, #from email
            ['optimuskrajm@gmail.com'], #to email
            fail_silently=False,
            )
            messages.success(request, 'Thank you for your time!')
            return redirect('first_meeting')

        return render(request, 'first_meeting.html', {'form':form, 'message_first_name':message_first_name})

class BlogPostView(View):
    form=BlogForm
    def get(self, request, *args, **kwargs):
        form = BlogForm
        return render(request, 'addPost.html', {"form":form})
    
    def post(self, request, *args, **kwargs):
        form=BlogForm
        form=self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addPost')
        return render(request, 'addPost.html', {"form":form})

def BlogDetails(request, pk):
    details = Blog.objects.get(id=pk)
    return render(request, "BlogDetails.html", {"details":details})