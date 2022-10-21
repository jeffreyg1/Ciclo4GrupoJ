"""
Modelo para la coleccion productos del webstore
@misiontic2022
"""
class Products:
    #Constructor de la clase
    def __init__(self,nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
    def toDBCollection(self):
        return {
            'nombre': self.nombre,
            'precio':self.precio,
            'cantidad':self.cantidad
        }