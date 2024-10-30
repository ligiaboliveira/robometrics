from rest_framework import serializers
from base.models import Cargo, Permissao, CargoPermissao, Equipe, Usuario, Robo, Sensor, RoboSensor, Pista, Corrida

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = '__all__'

class CargoPermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoPermissao
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robo
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class RoboSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoboSensor
        fields = '__all__'

class PistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pista
        fields = '__all__'

class CorridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrida
        fields = '__all__'
