from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def technology_blog(request):
    return render(request, 'technology-blog/blog.html')
