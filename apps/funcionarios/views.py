from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (UpdateView,
                                  ListView,
                                  DeleteView,
                                  CreateView)
from .models import Funcionario


class EditarFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = '/'


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa)


class DeletaFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:funcionarios_list')


class FuncionariosNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name = 'funcionarios/novo.html'
    success_url = '/funcionarios/'


    def form_valid(self, form):
        funcionario = form.save(commit=False)
        usuario = funcionario.nome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create_user(username=usuario)
        return super(FuncionariosNovo, self).form_valid(form)
