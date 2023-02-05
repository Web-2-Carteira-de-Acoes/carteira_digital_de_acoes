from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

def index(request):
    # return render(request, 'indexTest.html')
    
    return TemplateView.as_view(template_name="index.html")


def dashboard(request):
    # return render(request, 'indexTest.html')
    
    if request.method == 'GET':
        return render(request, 'dashboard.html')
    else:
        return render(request, 'dashboard.html')
    # return TemplateView.as_view(template_name="dashboard.html")
