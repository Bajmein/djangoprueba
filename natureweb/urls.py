"""
URL configuration for natureweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from natureapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='registro'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name="logout"),
    path('paisajes/', views.paisajes, name='paisajes'),
    path('paisajes/paisaje1/', views.paisaje1, name='paisaje1'),
    path('paisajes/paisaje2/', views.paisaje2, name='paisaje2'),
    path('paisajes/paisaje3/', views.paisaje3, name='paisaje3'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('comentarios/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('comentarios/<int:comentario_id>/eliminar', views.eliminar_comentario, name='eliminar_comentario')

]
