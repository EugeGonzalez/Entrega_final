from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import  DetailView
from django.views.generic.edit import DeleteView
from .form import Formulario_post, Buscar_post
from .models import Post




@login_required
def formulario_posteo(request):
    if request.method == 'POST':
        form = Formulario_post(request.POST, files=request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            msj = form.cleaned_data['titulo']   
            posteo = Post(titulo=data['titulo'], subtitulo=data['subtitulo'], texto=data['texto'], autor=data['autor'], imagen=data['imagen_post'])
            posteo.save()
            return render(request, "Inicio/index.html", {'msj':f'Se creo el post "{msj}"'})
        else:
            return render(request, "Posts/formulario_post.html", {'form':form})

    form = Formulario_post()
    return render(request, "Posts/formulario_post.html", {'form':form})



def lista_post(request):
    buscar_post = request.GET.get('titulo',None)

    if buscar_post is not None:
        posts = Post.objects.filter(titulo__icontains=buscar_post)
    else:
        posts = Post.objects.all()
        
    form = Buscar_post()
    return render(request, "Posts/lista_posts.html", {'form':form,'posts':posts})


class DeletePost(DeleteView):
   model = Post
   template_name = 'Posts/Post_confirm_delete.html'
   success_url = reverse_lazy('blog')


class DetallePost(DetailView):
    model = Post
    template_name = 'Posts/post_detail.html'


