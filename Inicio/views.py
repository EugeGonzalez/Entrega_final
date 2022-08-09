from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Usuarios.views import buscar_url_avatar
from Posts.models import Post


def inicio (request): 
    if request.user.is_authenticated:
        return render(request, "Inicio/index.html",{'user_avatar':buscar_url_avatar(request.user)}) 
    else:
        return render(request, "Inicio/index.html")

@login_required
def nosotros (request): 
    return render (request,'Inicio/nosotros.html',{'user_avatar':buscar_url_avatar(request.user)})


@login_required
def blog (request):
    posts = Post.objects.all()
    return render(request, "Inicio/blog.html",{'posts': posts, 'user_avatar':buscar_url_avatar(request.user)}) 


