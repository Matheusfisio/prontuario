from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evolucao
from pacientes.models import Paciente
from .forms import EvolucaoForm
from django.utils import timezone

@login_required
def evolucoes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    evolucoes = Evolucao.objects.filter(paciente=paciente)
    return render(request, 'evolucoes/lista.html', {'paciente': paciente, 'evolucoes': evolucoes})

@login_required
def nova_evolucao(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = EvolucaoForm(request.POST)
        if form.is_valid():
            nova = form.save(commit=False)
            nova.paciente = paciente
            nova.fisioterapeuta = request.user
            nova.save()
            return redirect('lista_evolucoes_paciente', paciente_id=paciente.id)
    else:
        form = EvolucaoForm()
    return render(request, 'evolucoes/form.html', {'form': form, 'paciente': paciente})

@login_required
def editar_evolucao(request, evolucao_id):
    evolucao_original = get_object_or_404(Evolucao, id=evolucao_id)
    if request.method == 'POST':
        form = EvolucaoForm(request.POST)
        if form.is_valid():
            nova = form.save(commit=False)
            nova.paciente = evolucao_original.paciente
            nova.fisioterapeuta = request.user
            nova.original = evolucao_original
            nova.editado_em = timezone.now()
            nova.save()
            return redirect('lista_evolucoes_paciente', paciente_id=evolucao_original.paciente.id)
    else:
        form = EvolucaoForm(instance=evolucao_original)
    return render(request, 'evolucoes/form.html', {'form': form, 'paciente': evolucao_original.paciente})

@login_required
def lista_evolucoes(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    evolucoes = paciente.evolucoes.all().order_by('-data')
    return render(request, 'pacientes/lista_evolucoes.html', {'paciente': paciente, 'evolucoes': evolucoes})
    

@login_required
def nova_evolucao(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = EvolucaoForm(request.POST)
        if form.is_valid():
            evolucao = form.save(commit=False)
            evolucao.paciente = paciente
            evolucao.fisioterapeuta = request.user
            evolucao.save()
            return redirect('evolucoes:lista_evolucoes', paciente_id=paciente.id)
    else:
        form = EvolucaoForm()
    return render(request, 'pacientes/form_evolucao.html', {'form': form, 'paciente': paciente})

@login_required
def listar_pacientes_para_evolucao(request):
    pacientes = Paciente.objects.filter(fisioterapeuta=request.user)
    return render(request, 'evolucoes/pacientes_para_evolucao.html', {
        'pacientes': pacientes
    })

@login_required
def lista_evolucoes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    evolucoes = Evolucao.objects.filter(paciente=paciente).order_by('-criado_em')
    return render(request, 'evolucoes/lista_evolucoes_paciente.html', {'paciente': paciente, 'evolucoes': evolucoes})

@login_required
def lista_pacientes_com_evolucao(request):
    pacientes = Paciente.objects.filter(fisioterapeuta=request.user)
    return render(request, 'evolucoes/lista_pacientes.html', {'pacientes': pacientes})