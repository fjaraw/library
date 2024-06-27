from registro_conductores.models import Conductor, Vehiculo, Direccion

def crear_conductor(nombre, apellido, fecha_nac):
    conductor = Conductor(nombre = nombre, apellido = apellido, fecha_nac = fecha_nac)
    conductor.save()

def agregar_direccion_a_conductor(calle, numero, comuna, region, conductor_id):
    d = Direccion(calle = calle, numero = numero, comuna = comuna, region = region, conductor_id = conductor_id)
    d.save()

def imprimir_modelos():
    conductores = Conductor.objects.all()
    direcciones = Direccion.objects.all()
    print(conductores)
    print(direcciones)