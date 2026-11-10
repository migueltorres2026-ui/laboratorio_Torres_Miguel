from datetime import date
from conexion import Session
from modelo import Estudiante, Equipo, Prestamo

def actualizar_estudiante(id_estudiante, nombre, correo):
    if type(id_estudiante) is not int or id_estudiante <= 0:
         raise ValueError("valor mayor a cero")

    nombre = nombre.strip()
    correo = correo.strip()

    if not nombre or len(nombre) <= 0:
         raise ValueError("tener caracteres")
    if not correo or len(correo) <= 0:
         raise ValueError("tener caracteres")

    with Session.begin() as session:
          estudiante = session.get(Estudiante, id_estudiante)
          if estudiante is None:
               return False
          
          estudiante.nombre = nombre
          estudiante.correo = correo
    return True

def actualizar_Equipo(id_equipo,nombre, tipo, stock_disponible):
    if not type(id_equipo) is int or id_equipo <= 0:
         raise ValueError("valor mayor a cero")
    
    nombre = nombre.strip()
    tipo = tipo.strip()

    if not nombre or len(nombre) <= 0:
        raise ValueError("tener caracteres")
    if not tipo or len(tipo) <= 0:
        raise ValueError("tener caracteres")
    if not type(stock_disponible) is int or stock_disponible < 0:
        raise ValueError("valor mayor a cero")

    with Session.begin() as session:
         equipo = session.get(Equipo, id_equipo)
         if equipo is None:
              return False

         equipo.nombre = nombre
         equipo.tipo = tipo
         equipo.stock_disponible = stock_disponible
    return True


def actualizar_prestamo(id_prestamo, id_equipo, id_estudiante, cantidad, fecha):
    if type(id_estudiante) is not int or id_estudiante <= 0:
         raise ValueError("valor mayor a cero")

    if not type(id_equipo) is int or id_equipo <= 0:
         raise ValueError("valor mayor a cero")
    
    if not type(id_prestamo) is int or id_prestamo <= 0:
         raise ValueError("valor mayor a cero")    
    
    if not type(cantidad) is int or cantidad < 0:
          raise ValueError("no debe ser menor a cero")
    
    if type(fecha) is not date:
          raise ValueError("La fecha debe ser un objeto date")
    
    with Session.begin() as session:
         prestamo = session.get(Prestamo, id_equipo, id_estudiante, id_prestamo)
         if prestamo is None:
              return False

         prestamo.cantidad = cantidad
         prestamo.fecha = fecha
    return True