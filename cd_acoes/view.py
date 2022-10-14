from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    # return render(request, 'indexTest.html')
    
    return TemplateView.as_view(template_name="index.html")
