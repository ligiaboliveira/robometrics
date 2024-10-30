from django.core.management.base import BaseCommand
from base.models import Cargo, Permissao, CargoPermissao, Equipe, Usuario, Robo, Sensor, RoboSensor, Pista, Corrida
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Delete all entries in the database'

    def handle(self, *args, **kwargs):
        # Order of deletion is important due to foreign key constraints
        models = [Corrida, RoboSensor, Robo, Sensor, Usuario, CargoPermissao, Permissao, Cargo, Equipe, Pista, User]

        for model in models:
            model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'All entries in {model.__name__} deleted successfully'))

        self.stdout.write(self.style.SUCCESS('All database entries deleted successfully'))