# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Pista
from api.serializers import PistaSerializer

@api_view(['GET'])
def get_pistas(request):
    pistas = Pista.objects.all()
    serializer = PistaSerializer(pistas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_pista(request):
    serializer = PistaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_pista(request, pk):
    try:
        pista = Pista.objects.get(pk=pk)
    except Pista.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PistaSerializer(pista)
    return Response(serializer.data)

@api_view(['PUT'])
def update_pista(request, pk):
    try:
        pista = Pista.objects.get(pk=pk)
    except Pista.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PistaSerializer(instance=pista, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pista(request, pk):
    try:
        pista = Pista.objects.get(pk=pk)
    except Pista.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pista.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)