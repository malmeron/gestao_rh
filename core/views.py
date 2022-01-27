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


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]