# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Corrida
from api.serializers import CorridaSerializer

@api_view(['GET'])
def get_corridas(request):
    corridas = Corrida.objects.all()
    serializer = CorridaSerializer(corridas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_corrida(request):
    serializer = CorridaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_corrida(request, pk):
    try:
        corrida = Corrida.objects.get(pk=pk)
    except Corrida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CorridaSerializer(corrida)
    return Response(serializer.data)

@api_view(['PUT'])
def update_corrida(request, pk):
    try:
        corrida = Corrida.objects.get(pk=pk)
    except Corrida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CorridaSerializer(instance=corrida, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_corrida(request, pk):
    try:
        corrida = Corrida.objects.get(pk=pk)
    except Corrida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    corrida.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)