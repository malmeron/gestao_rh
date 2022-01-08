from django.urls import path
from .views import DocumentoCreate#, DocumentoDelete

urlpatterns = [
        path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(),name='create_documento'),
    #path('deletar/<int:pk>/', DocumentoDelete.as_view(),name='delete_empresa'),
]
