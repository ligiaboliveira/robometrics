from django.core.management.base import BaseCommand
from base.models import Cargo, Permissao, CargoPermissao, Equipe, Usuario, Robo, Sensor, RoboSensor, Pista, Corrida
from datetime import datetime
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Create Cargo
        cargo1 = Cargo.objects.create(nome='Cargo 1')
        cargo2 = Cargo.objects.create(nome='Cargo 2')

        # Create Permissao
        permissao1 = Permissao.objects.create(nome='Permissao 1')
        permissao2 = Permissao.objects.create(nome='Permissao 2')

        # Create CargoPermissao
        CargoPermissao.objects.create(id_cargo=cargo1, id_permissao=permissao1)
        CargoPermissao.objects.create(id_cargo=cargo2, id_permissao=permissao2)

        # Create Equipe
        equipe1 = Equipe.objects.create(equipe='Garagino')

        # Create Usuario
        Usuario.objects.create(nome='User 1', email='user1@example.com', senha='password1', id_cargo=cargo1, id_equipe=equipe1)
        Usuario.objects.create(nome='User 2', email='user2@example.com', senha='password2', id_cargo=cargo2, id_equipe=equipe1)
        
        User.objects.create_user(username='admin', email='admin@example.com', password='adminpassword')
        User.objects.create_user(username='user', email='user@example.com', password='userpassword')

        # Create Robo
        robo1 = Robo.objects.create(id_equipe=equipe1, tipo='Tipo 1')
        robo2 = Robo.objects.create(id_equipe=equipe1, tipo='Tipo 2')

        # Create Sensor
        sensor1 = Sensor.objects.create(sensores='Sensor 1')
        sensor2 = Sensor.objects.create(sensores='Sensor 2')

        # Create RoboSensor
        RoboSensor.objects.create(id_robo=robo1, id_sensores=sensor1, periodo_ativacao=datetime.now().date())
        RoboSensor.objects.create(id_robo=robo2, id_sensores=sensor2, periodo_ativacao=datetime.now().date())

        # Create Pista
        pista1 = Pista.objects.create(pista='Pista 1')
        pista2 = Pista.objects.create(pista='Pista 2')

        # Create Corrida
        Corrida.objects.create(id_pista=pista1, id_robos=robo1, log_corrida='Log 1', P=1.0, I=0.1, D=0.01, tempo=60.0)
        Corrida.objects.create(id_pista=pista2, id_robos=robo2, log_corrida='Log 2', P=2.0, I=0.2, D=0.02, tempo=120.0)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))