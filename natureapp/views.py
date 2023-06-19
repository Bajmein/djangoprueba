from django.shortcuts import render, redirect, get_object_or_404
from natureapp.forms import UserForm, PaisajeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Comentarios
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserForm})
    else:
        try:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            user.save()
            login(request, user)
            return redirect('home')

        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserForm,
                'error': 'El usuario ya existe'
            })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': UserForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
                'form': UserForm,
                'error': 'El nombre de usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('paisajes')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


@login_required
def paisajes(request):
    return render(request, 'paisajes.html')


@login_required
def paisaje1(request):
    if request.method == 'GET':
        return render(request, 'paisaje1.html', {
            'form': PaisajeForm
        })
    else:
        try:
            form = PaisajeForm(request.POST)
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.user = request.user
            nuevo_comentario.save()
            return redirect('/comentarios/')
        except ValueError:
            return render(request, 'paisaje1.html', {
                'form': PaisajeForm,
                'error': 'Entregar datos validos'
            })


@login_required()
def paisaje2(request):
    if request.method == 'GET':
        return render(request, 'paisaje2.html', {
            'form': PaisajeForm
        })
    else:
        try:
            form = PaisajeForm(request.POST)
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.user = request.user
            nuevo_comentario.save()
            return redirect('/comentarios/')
        except ValueError:
            return render(request, 'paisaje2.html', {
                'form': PaisajeForm,
                'error': 'Entregar datos validos'
            })


@login_required()
def paisaje3(request):
    if request.method == 'GET':
        return render(request, 'paisaje3.html', {
            'form': PaisajeForm
        })
    else:
        try:
            form = PaisajeForm(request.POST)
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.user = request.user
            nuevo_comentario.save()
            return redirect('/comentarios/')
        except ValueError:
            return render(request, 'paisaje3.html', {
                'form': PaisajeForm,
                'error': 'Entregar datos validos'
            })


@login_required
def comentarios(request):
    post = Comentarios.objects.filter(user=request.user)
    return render(request, 'comentarios.html', {
        'comentarios': post
    })


@login_required
def editar_comentario(request, comentario_id):
    if request.method == 'GET':
        comentario = get_object_or_404(Comentarios, pk=comentario_id, user=request.user)
        form = PaisajeForm(instance=comentario)
        return render(request, 'editar_comentario.html', {
            'comentario': comentario,
            'form': form
        })
    else:
        try:
            comentario = get_object_or_404(Comentarios, pk=comentario_id, user=request.user)
            form = PaisajeForm(request.POST, instance=comentario)
            form.save()
            return redirect('comentarios')
        except ValueError:
            return render(request, 'editar_comentario.html', {
                'comentario': comentario,
                'form': form,
                'error': 'Error al editar comentario'
            })


@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, pk=comentario_id, user=request.user)
    if request.method == 'POST':
        comentario.delete()
        return redirect('comentarios')
