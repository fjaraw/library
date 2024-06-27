from django.core.management.base import BaseCommand
from registro_conductores.services import *
# se ejecuta: python manage.py test_client
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #probar que se pueda agregar un nuevo Cliente
        print('Testeo de programa')
        #crear_conductor('John','Doe','1970-01-01')
        #agregar_direccion_a_conductor('Av. Rocadura', '1010', 'Piedradura','v',1)
        #crear_conductor('Jane','Doe','1970-01-01')
        #agregar_direccion_a_conductor('Caldera', '1010', 'Copiapó','iii',2)
        imprimir_modelos()
        print('Operación realizada.')