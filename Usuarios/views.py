from django.shortcuts import render
from re import I
from django.contrib.auth import login as Login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import form_register, form_edit_user
from .models import NuestroUser


def register (request): 
    if request.method == 'POST':

        form = form_register(request.POST,request.FILES)
        

        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Inicio/index.html", {'msj':f'Se creo el usuario {username}'})
        else:
            return render(request, "Usuarios/register.html", {'form':form})
    form = form_register()
    return render(request, "Usuarios/register.html", {'form':form})
  

def login (request): 

    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not  None:
                Login(request, user)
                return render(request, "Inicio/index.html", {'msj':f'Bienvenido {username}!'})
            else:
                return render(request, 'Usuarios/login.html', {'form':form})

        else:
            return render(request, 'Usuarios/login.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'Usuarios/login.html', {'form':form})




@login_required
def editar (request):
    
    usuario_extendido, _ = NuestroUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = form_edit_user(request.POST,request.FILES)

        if form.is_valid():
            
            data = form.cleaned_data
            logued_user = request.user 
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name',)
            logued_user.last_name = data.get('last_name')
            usuario_extendido.imagen = data['imagen']
            usuario_extendido.link= data['link']
            usuario_extendido.bio = data['bio']


            if data.get('password1') == data.get('password2') and len(data.get("password1")) >8:
                logued_user.set_password(data.get('password1'))
                msj = 'Se actualizo la contrase??a' 
            else:
                msj = 'No se cambio la contrase??a'

            logued_user.save()
            usuario_extendido.save()
            
            return render(request, "Inicio/index.html", {'msj':msj})
        else:
            return render(request, "Inicio/index.html", {'form':form, 'msj':''})

        
        
    form = form_edit_user(
        initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'imagen': usuario_extendido.imagen,
            'link': usuario_extendido.link,
            'bio': usuario_extendido.bio
        }
    )
    return render(request, "Usuarios/editar_user.html", {'form':form, 'msj':''})




def perfil(request):
    mas_datos, _ = NuestroUser.objects.get_or_create(user=request.user)
    return render(request, "Usuarios/perfil_user.html", {'mas_datos':mas_datos})




def buscar_url_avatar(user):

    usuario_extendido, _ = NuestroUser.objects.get_or_create(user=user)
    if usuario_extendido.imagen:
        return usuario_extendido.imagen.url
    else:
        return 'https://www.gravatar.com/avatar/' 


