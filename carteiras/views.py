from django.shortcuts import render, redirect
from .models import Carteira
from .forms import CarteiraForm


def list_carteiras(request):
    carteiras = Carteira.objects.all()
    return render(request, 'list_carteiras.html', {'carteiras': carteiras})


def create_carteira(request):
    form = CarteiraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_carteiras')

    return render(request, 'carteiras-form.html', {'form': form})


def update_carteira(request, id):
    carteira = Carteira.objects.get(id=id)
    form = CarteiraForm(request.POST or None, instance=carteira)

    if form.is_valid():
        form.save()
        return redirect('list_carteiras')

    return render(request, 'carteiras-form.html', {'form': form, 'carteira': carteira})


def delete_carteira(request, id):
    carteira = Carteira.objects.get(id=id)

    if request.method == 'POST':
        carteira.delete()
        return redirect('list_carteiras')

    return render(request, 'carteira-delete-confirm.html', {'carteira': carteira})