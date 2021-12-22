from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa
# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome',]

    #Sobrescrevendo o método de validação do formulário
    #Para atribuir a empresa que está sendo editada para o usuário que está logado
    def form_valid(self, form):
        obj = form.save() #aqui eu tenho o objeto empresa em mãos
        funcionario = self.request.user.funcionario  #aqui eu tenho o objeto funcionário em mãos
        funcionario.empresa = obj
        funcionario.save()
        #return HttpResponse('ok') # só para debugar para ver se deu certo!

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome',]