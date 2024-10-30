# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Cargo
from api.serializers import CargoSerializer

@api_view(['GET'])
def get_cargos(request):
    cargos = Cargo.objects.all()
    serializer = CargoSerializer(cargos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_cargo(request):
    serializer = CargoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_cargo(request, pk):
    try:
        cargo = Cargo.objects.get(pk=pk)
    except Cargo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CargoSerializer(cargo)
    return Response(serializer.data)

@api_view(['PUT'])
def update_cargo(request, pk):
    try:
        cargo = Cargo.objects.get(pk=pk)
    except Cargo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CargoSerializer(instance=cargo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_cargo(request, pk):
    try:
        cargo = Cargo.objects.get(pk=pk)
    except Cargo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cargo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)