from datetime import date
from conexion import Session
from modelo import Equipo, Estudiante, Prestamo

def registrar_Equipo(nombre, tipo, stock_disponible):
    nombre = nombre.strip()
    tipo = tipo.strip()

    if not nombre or len(nombre) <= 0:
        raise ValueError("tener caracteres")
    if not tipo or len(tipo) <= 0:
        raise ValueError("tener caracteres")
    if not type(stock_disponible) is int or stock_disponible < 0:
        raise ValueError("valor mayor a cero")

    with Session as session:

        equipo = Equipo(
        nombre = nombre,
        tipo = tipo,
        stock_disponible = stock_disponible)
    session.add(equipo)
    return equipo

def registrar_Estudiante(nombre, correo):
        nombre = nombre.strip()
        correo = correo.strip()
        if not nombre or len(nombre) <= 0:
             raise ValueError("tener caracteres")
        if not correo or len(correo) <= 0:
             raise ValueError("tener caracteres")

        with Session as session:
             estudiante = Estudiante(
                  nombre = nombre,
                  correo = correo
             )
        session.add(estudiante)
        return estudiante

def registrar_Prestamo(fecha, cantidad):
     if not type(cantidad) is int or cantidad < 0:
          raise ValueError("no debe ser menor a cero")
     if type(fecha) is not date:
          raise ValueError("La fecha debe ser un objeto date")

     with Session as session:
          prestamo =  Prestamo(
               fecha = fecha,
               cantidad = cantidad
          )
          session.add(prestamo)
          return prestamo
