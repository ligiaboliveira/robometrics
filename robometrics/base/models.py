from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Permissao(models.Model):
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class CargoPermissao(models.Model):
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    id_permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Equipe(models.Model):
    equipe = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    id_equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Robo(models.Model):
    id_equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nome_robo = models.CharField(max_length=255, default='Nome Padrão')
    tipo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Sensor(models.Model):
    sensores = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class RoboSensor(models.Model):
    id_robo = models.ForeignKey(Robo, on_delete=models.CASCADE)
    id_sensores = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    periodo_ativacao = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Pista(models.Model):
    pista = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Corrida(models.Model):
    id_pista = models.ForeignKey(Pista, on_delete=models.CASCADE, null=True)
    id_robos = models.ForeignKey(Robo, on_delete=models.CASCADE, null=True)
    log_corrida = models.CharField(max_length=255, null=True)
    P = models.FloatField(null=True)     # Define P as a FloatField
    I = models.FloatField(null=True)     # Define I as a FloatField
    D = models.FloatField(null=True)     # Define D as a FloatField
    tempo = models.FloatField(null=True) # Define tempo as a FloatField
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    
