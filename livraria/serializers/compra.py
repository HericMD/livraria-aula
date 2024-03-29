from rest_framework.serializers import ModelSerializer, CharField

from livraria.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ["livro", "quantidade"]
        depth = 1

class CompraSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True, read_only=True)
    class Meta:
        model = Compra
        fields = ["id", "usuario", "status", "itens"]