
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import FormularioAvaliacao
from django.contrib.auth.decorators import login_required
import json

@login_required
def editor_formulario(request):
    if request.method == "POST":
        data = json.loads(request.body)
        formulario, _ = FormularioAvaliacao.objects.update_or_create(
            profissional=request.user,
            nome=data.get("nome", "Avaliação"),
            defaults={"estrutura_json": data.get("estrutura", {})}
        )
        return JsonResponse({"status": "salvo", "id": formulario.id})
    return render(request, "editor.html")

@login_required
def carregar_formulario(request, id):
    formulario = get_object_or_404(FormularioAvaliacao, id=id, profissional=request.user)
    return JsonResponse(formulario.estrutura_json, safe=False)
