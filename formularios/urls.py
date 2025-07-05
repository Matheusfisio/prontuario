
from django.urls import path
from . import views

urlpatterns = [
    path("editor/", views.editor_formulario, name="editor_formulario"),
    path("carregar/<int:id>/", views.carregar_formulario, name="carregar_formulario"),
   

]
