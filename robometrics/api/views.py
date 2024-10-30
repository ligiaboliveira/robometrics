from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Cargo, Permissao, CargoPermissao, Equipe, Usuario, Robo, Sensor, RoboSensor, Pista, Corrida
from .serializers import CargoSerializer, PermissaoSerializer, CargoPermissaoSerializer, EquipeSerializer, UsuarioSerializer, RoboSerializer, SensorSerializer, RoboSensorSerializer, PistaSerializer, CorridaSerializer

@api_view(['GET'])
def getCargos(request):
    cargos = Cargo.objects.all()
    serializer = CargoSerializer(cargos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPermissoes(request):
    permissoes = Permissao.objects.all()
    serializer = PermissaoSerializer(permissoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCargosPermissoes(request):
    cargos_permissoes = CargoPermissao.objects.all()
    serializer = CargoPermissaoSerializer(cargos_permissoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEquipes(request):
    equipes = Equipe.objects.all()
    serializer = EquipeSerializer(equipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRobos(request):
    robos = Robo.objects.all()
    serializer = RoboSerializer(robos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSensores(request):
    sensores = Sensor.objects.all()
    serializer = SensorSerializer(sensores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRobosSensores(request):
    robos_sensores = RoboSensor.objects.all()
    serializer = RoboSensorSerializer(robos_sensores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPistas(request):
    pistas = Pista.objects.all()
    serializer = PistaSerializer(pistas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCorridas(request):
    corridas = Corrida.objects.all()
    serializer = CorridaSerializer(corridas, many=True)
    return Response(serializer.data)