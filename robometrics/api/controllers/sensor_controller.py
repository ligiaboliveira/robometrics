# api/cargo_controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Sensor
from api.serializers import SensorSerializer

@api_view(['GET'])
def get_sensores(request):
    sensores = Sensor.objects.all()
    serializer = SensorSerializer(sensores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_sensor(request):
    serializer = SensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_sensor(request, pk):
    try:
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SensorSerializer(sensor)
    return Response(serializer.data)

@api_view(['PUT'])
def update_sensor(request, pk):
    try:
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SensorSerializer(instance=sensor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_sensor(request, pk):
    try:
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    sensor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)