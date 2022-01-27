from funcionarios.models import Funcionario
from rest_framework import serializers
from registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):

    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['id','nome', 'departamentos', 'empresa', 'user', 'total_horas_extra','registrohoraextra_set']
        # No total_horas_extra como é uma property pode apenas incluir
        #Se fosse um método não poderia fazer dessa maneira

        # Para buscar no shell
        #python manage.py shell
        #from funcionarios.models import *
        #f = Funcionario.objects.last()
        #dir(f)
        #'registrohoraextra_set'

        # Agora que foi adicionado o id pode chamar pelo id somente um funcionário, exemplo
        # http://127.0.0.1:8000/api/funcionarios/1/

