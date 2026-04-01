from django.urls import path
from django.views.generic import RedirectView
from .views import Empresas, VagasEmpresa, InscricaoVaga, Sucesso

urlpatterns = [
    path("", RedirectView.as_view(url="/empresas/"), name="home"),
    path("empresas/", Empresas.as_view(), name="empresas"),
    path("empresas/<int:empresa_id>/vagas/", VagasEmpresa.as_view(), name="vagas_empresa"),
    path("vagas/<int:vaga_id>/inscrever/", InscricaoVaga.as_view(), name="inscricao_vaga"),
    path("sucesso/", Sucesso.as_view(), name="sucesso"),
]
