from django.shortcuts import render
from django.utils import timezone
from .models import DatosB
from django.shortcuts import render, get_object_or_404
from .forms import DatosForm
from django.shortcuts import redirect



# Create your views here.
def datos_list(request):
    posts = DatosB.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/datos_list.html', {'posts': posts})

def datos_detail(request, pk):
    post = get_object_or_404(DatosB, pk=pk)
    return render(request, 'blog/datos_detail.html', {'post': post})
    DatosB.objects.get(pk=pk) 


def datos_new(request):
    if request.method == "POST":
        form = DatosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('datos_detail', pk=post.pk)
    else:
        form = DatosForm()
    return render(request, 'blog/datos_edit.html', {'form': form})

def datos_edit(request, pk):
    post = get_object_or_404(DatosB, pk=pk)
    if request.method == "POST":
        form = DatosForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('datos_detail', pk=post.pk)
    else:
        form = DatosForm(instance=post)
    return render(request, 'blog/datos_edit.html', {'form': form})

def datos_delete(request, pk):
    post = get_object_or_404(DatosB, pk=pk)
    post = DatosB.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('datos_list')
    else:
        form = DatosForm(instance=post)
    return render(request, 'blog/datos_delete.html', {'post': post})