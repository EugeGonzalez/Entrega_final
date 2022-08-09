from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="index"),
    path('logout/', LogoutView.as_view(template_name="Usuarios/logout.html"), name='logout'),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('blog/', views.blog, name="blog"),
]