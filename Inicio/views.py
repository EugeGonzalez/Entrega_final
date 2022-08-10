from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Usuarios.views import buscar_url_avatar
from Posts.models import Post


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


