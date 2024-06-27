from django.core.management.base import BaseCommand
from books_and_authors.models import Client
# se ejecuta: python manage.py test_client
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #probar que se pueda agregar un nuevo Cliente
        print('Hola!')
        c = Client(first_name="José", last_name="Jara", email="xyz@xyz.com", height = 1.76)
        c.save()
        print('Cliente creado.')