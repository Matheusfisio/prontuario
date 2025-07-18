from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from django.views.decorators.http import require_GET
from datetime import datetime, time, timezone
from .models import Agendamento
from .forms import AgendamentoForm
from django.http import JsonResponse


def geren_agenda(request):
    return render(request, 'agendamentos/agenda_inicio.html')

@login_required
def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    else:
        form = AgendamentoForm()
        return render(request, 'agendamentos/partials/form_agendamento.html', {

            'form': form,
            'form_action': reverse('agendamentos:novo_agendamento')
        })


@login_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    else:
        form = AgendamentoForm(instance=agendamento)
        return render(request, 'agendamentos/partials/form_agendamento.html', {

            'form': form,
            'form_action': reverse('agendamentos:editar_agendamento', args=[agendamento.id])
        })

@login_required
def excluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == 'POST':
        agendamento.delete()
        return JsonResponse({'success': True})  # ou redirect conforme sua lógica

    return render(request, 'agendamentos/excluir_agendamento.html', {'agendamento': agendamento})


def buscar_agendamentos_por_data(request, data_str):
    from datetime import datetime
    data = datetime.strptime(data_str, "%Y-%m-%d").date()
    agendamentos = Agendamento.objects.filter(data=data).select_related('paciente', 'fisioterapeuta')
    
    response_data = [
        {
            "horario": ag.horario.strftime("%H:%M"),
            "paciente": ag.paciente.nome,
            "fisioterapeuta": ag.fisioterapeuta.nome,
        }
        for ag in agendamentos
    ]
    return JsonResponse(response_data, safe=False)

from django.http import JsonResponse
from .models import Agendamento



@require_GET
def horarios_por_data(request):
    data = request.GET.get('data')
    if data:
        agendamentos = Agendamento.objects.filter(data=data).order_by('hora_inicio')
        horarios = [f"{a.hora_inicio.strftime('%H:%M')} - {a.fisioterapeuta} - {a.paciente}" for a in agendamentos]
    else:
        horarios = []

    return JsonResponse({'horarios': horarios})

@login_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    eventos = []

    for ag in agendamentos:
        eventos.append({
            "id": ag.id,
            "title": ag.titulo,
            "start": ag.inicio.isoformat(),
            "end": ag.fim.isoformat(),
        })

    return JsonResponse(eventos, safe=False)

@require_GET
def eventos_json(request):
    agendamentos = Agendamento.objects.all()
    eventos = [
        {
            'id': a.id,  # <-- IMPORTANTE
            'title': f'{a.paciente.nome} - {a.fisioterapeuta.first_name}',
            'start': f'{a.data}T{a.hora_inicio}',
        }
        for a in agendamentos
    ]
    return JsonResponse(eventos, safe=False)


@require_GET
def horarios_json(request):
    data_str = request.GET.get('data')
    data = parse_date(data_str)

    agendamentos = Agendamento.objects.filter(data=data).order_by('hora_inicio')
    horarios = [f"{a.hora_inicio.strftime('%H:%M')} - {a.hora_fim.strftime('%H:%M')} ({a.paciente.nome})" for a in agendamentos]

    return JsonResponse({"horarios": horarios})



@login_required
def pagina_agenda(request):
    return render(request, 'agendamentos/agenda.html')

