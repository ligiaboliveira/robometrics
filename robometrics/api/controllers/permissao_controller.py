# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Permissao
from api.serializers import PermissaoSerializer

@api_view(['GET'])
def get_permissoes(request):
    permissoes = Permissao.objects.all()
    serializer = PermissaoSerializer(permissoes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_permissao(request):
    serializer = PermissaoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_permissao(request, pk):
    try:
        permissao = Permissao.objects.get(pk=pk)
    except Permissao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PermissaoSerializer(permissao)
    return Response(serializer.data)

@api_view(['PUT'])
def update_permissao(request, pk):
    try:
        permissao = Permissao.objects.get(pk=pk)
    except Permissao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PermissaoSerializer(instance=permissao, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_permissao(request, pk):
    try:
        permissao = Permissao.objects.get(pk=pk)
    except Permissao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    permissao.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)