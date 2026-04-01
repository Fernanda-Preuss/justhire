from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy
from .models import Empresa, Vaga
from .forms import InscricaoForm


class Empresas(ListView):
    model = Empresa
    template_name = "website/empresas.html"
    context_object_name = "empresas"


class VagasEmpresa(ListView):
    template_name = "website/vagas.html"
    context_object_name = "vagas"

    def get_queryset(self):
        return Vaga.objects.filter(empresa_id=self.kwargs['empresa_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.get(id=self.kwargs['empresa_id'])
        return context


class InscricaoVaga(FormView):
    template_name = "website/inscricao.html"
    form_class = InscricaoForm
    success_url = reverse_lazy('sucesso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaga'] = Vaga.objects.get(id=self.kwargs['vaga_id'])
        return context

    def form_valid(self, form):
        inscricao = form.save(commit=False)
        inscricao.vaga = Vaga.objects.get(id=self.kwargs['vaga_id'])
        inscricao.save()
        return super().form_valid(form)


class Sucesso(TemplateView):
    template_name = "website/sucesso.html"
