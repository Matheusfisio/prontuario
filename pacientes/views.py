# Views for pacientesfrom django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

@login_required
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.criado_por = request.user
            paciente.usuario = request.user  # se existir esse campo
            paciente.fisioterapeuta = request.user  # obrigatório!
            paciente.save()
            return redirect('pacientes:lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form})

@login_required
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if paciente.criado_por != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes:lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form})

@login_required
def excluir_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes:lista_pacientes')
    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})

@login_required
def detalhes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    avaliacoes = Avaliacao.objects.filter(paciente=paciente)
    evolucoes = Evolucao.objects.filter(paciente=paciente)
    return render(request, 'pacientes/detalhes_paciente.html', {
        'paciente': paciente,
        'avaliacoes': avaliacoes,
        'evolucoes': evolucoes
    })
