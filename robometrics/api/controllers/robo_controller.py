# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Robo
from api.serializers import RoboSerializer

@api_view(['GET'])
def get_robos(request):
    robos = Robo.objects.all()
    serializer = RoboSerializer(robos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_robo(request):
    serializer = RoboSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_robo(request, pk):
    try:
        robo = Robo.objects.get(pk=pk)
    except Robo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RoboSerializer(robo)
    return Response(serializer.data)

@api_view(['PUT'])
def update_robo(request, pk):
    try:
        robo = Robo.objects.get(pk=pk)
    except Robo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RoboSerializer(instance=robo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_robo(request, pk):
    try:
        robo = Robo.objects.get(pk=pk)
    except Robo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    robo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)