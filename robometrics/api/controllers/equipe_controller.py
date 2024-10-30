# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Equipe
from api.serializers import EquipeSerializer


@api_view(['GET'])
def get_equipes(request):
    equipes = Equipe.objects.all()
    serializer = EquipeSerializer(equipes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_equipe(request):
    serializer = EquipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_equipe(request, pk):
    try:
        equipe = Equipe.objects.get(pk=pk)
    except Equipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EquipeSerializer(equipe)
    return Response(serializer.data)

@api_view(['PUT'])
def update_equipe(request, pk):
    try:
        equipe = Equipe.objects.get(pk=pk)
    except Equipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EquipeSerializer(instance=equipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_equipe(request, pk):
    try:
        equipe = Equipe.objects.get(pk=pk)
    except Equipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    equipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)