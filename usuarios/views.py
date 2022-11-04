from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm


def list_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'list_usuarios.html', {'usuarios': usuarios})


def create_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_usuarios')

    return render(request, 'usuarios-form.html', {'form': form})


def update_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('list_usuarios')

    return render(request, 'usuarios-form.html', {'form': form, 'usuario': usuario})


def delete_usuario(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('list_usuarios')

    return render(request, 'usuario-delete-confirm.html', {'usuario': usuario})