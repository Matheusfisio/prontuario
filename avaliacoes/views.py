
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Avaliacao
from pacientes.models import Paciente
from django.contrib.auth.decorators import login_required
import json
from .forms import AvaliacaoForm




def avaliacoes_inicio(request):
    pacientes = Paciente.objects.all()
    return render(request, 'avaliacoes/avaliacoes_inicio.html', {'pacientes': pacientes})

@login_required
def nova_avaliacao(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        area = request.POST.get('area')
        articulacao = request.POST.get('articulacao')

        # Captura todas as medidas dinamicamente
        medidas = {
            key.replace("medida_", ""): value
            for key, value in request.POST.items()
            if key.startswith("medida_") and value.strip() != ""
        }

        Avaliacao.objects.create(
            paciente=paciente,
            fisioterapeuta=request.user,
            area=area,
            articulacao=articulacao,
            medidas_json=medidas
        )

        return redirect('avaliacoes:lista_avaliacoes', paciente_id=paciente.id)

    return render(request, 'avaliacoes/nova_avaliacao.html', {'paciente': paciente})

@login_required
def listar_avaliacoes(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    avaliacoes = Avaliacao.objects.filter(paciente=paciente).order_by('-data')
    return render(request, 'avaliacoes/lista_avaliacoes.html', {
        'paciente': paciente,
        'avaliacoes': avaliacoes
    })

def editar_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacoes:lista_avaliacoes', paciente_id=avaliacao.paciente.id)
    else:
        form = AvaliacaoForm(instance=avaliacao)

    return render(request, 'avaliacoes/editar_avaliacao.html', {
        'form': form,
        'paciente': avaliacao.paciente
    })

def excluir_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    paciente_id = avaliacao.paciente.id
    avaliacao.delete()
    return redirect('avaliacoes:lista_avaliacoes', paciente_id=paciente_id)
