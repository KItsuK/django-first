from django.shortcuts import render

def index(request):
    """/toppage"""
    context = {
    'name':'Kanan'
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    """/aboutpage"""
    return render(request, 'myapp/about.html')

def info(request):
    """/infopage"""
    return render(request, 'myapp/info.html')
