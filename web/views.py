from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'Blog-posts.html', {})

def blog2(request):
    return render(request, 'Blog-posts-2.html', {})

def post(request):
    return render(request, 'Single-blog.html', {})

def projects(request):
    return render(request, 'Portfolio.html', {})

def project(request):
    return render(request, 'Portfolio-detail.html', {})

def galery(request):
    return render(request, 'Galery.html', {})

def contact(request):
    return render(request, 'Contact.html', {})