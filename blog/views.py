from django.shortcuts import render
from django.utils import timezone
from .models import DatosB
from django.shortcuts import render, get_object_or_404




# Create your views here.
def datos_list(request):
    posts = DatosB.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/datos_list.html', {'posts': posts})

def datos_detail(request, pk):
    post = get_object_or_404(DatosB, pk=pk)
    return render(request, 'blog/datos_detail.html', {'post': post})
    DatosB.objects.get(pk=pk) 