from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#importar funcionário para pegar os dados dele
from funcionarios.models import Funcionario

@login_required
def home(request):
    #dicionario para enviar os dados
    data = {}
    # capturando o usuario
    data['usuario'] = request.user

    return render(request,'core/index.html', data)