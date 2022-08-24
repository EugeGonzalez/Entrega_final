import dataclasses
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Usuarios.views import buscar_url_avatar
from Posts.models import Post
from Inicio.forms import *
from Inicio.models import *



def inicio (request): 
    if request.user.is_authenticated:
        return render(request, "Inicio/index.html") 
    else:
        return render(request, "Inicio/index.html")


def nosotros (request): 
    return render (request,'Inicio/nosotros.html')



def blog (request):
    posts = Post.objects.all()
    return render(request, "Inicio/blog.html") 


def contacto(request):
    if request.method == 'POST':

        form = contactoForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            
            contacto = Contacto(nombre=info["nombre"], email=info["email"],texto=dataclasses['texto'])
            contacto.save()
            return render (request, "Inicio/index.html")
        else:
            return render(request, "Inicio/contacto.html", {'form':form})
    else:
        form = contactoForm()
    return render(request, "Inicio/contacto.html", {"form":form})