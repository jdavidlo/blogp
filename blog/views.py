from django.shortcuts import render

# Create your views here.
def datos_list(request):
    return render(request, 'blog/datos_list.html', {})