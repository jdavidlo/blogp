from django.shortcuts import render
from django.utils import timezone
from .models import DatosB

# Create your views here.
def datos_list(request):
    posts = DatosB.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/datos_list.html', {'posts': posts})