import enum


from enum import Enum

precio_base = 100
class productos(Enum):
    ALIMENTACION = 1
    SERVICIOS = 2
if productos.ALIMENTACION:
    precio = precio_base+precio_base*0.055
if productos.SERVICIOS:
    precio = precio_base+precio_base*0.2
print(precio)