from datetime import date
from conexion import Session
from modelo import Estudiante, Equipo, Prestamo

def eliminar_estudiante(id_estudiante):
    if type(id_estudiante) is not int or id_estudiante <= 0:
         raise ValueError("valor mayor a cero")

    with Session.begin() as session:
         estudiante = session.get(Estudiante, id_estudiante)
         if estudiante is None:
              return False

         session.delete(estudiante)

def eliminar_equipo(id_equipo):
    if type(id_equipo) is not int or id_equipo <= 0:
         raise ValueError("valor mayor a cero")

    with Session.begin() as session:
         equipo = session.get(Equipo, id_equipo)
         if equipo is None:
              return False

         session.delete(equipo)

def eliminar_prestamo(id_prestamo, id_equipo, id_estudiante):
    if type(id_estudiante) is not int or id_estudiante <= 0:
         raise ValueError("valor mayor a cero")

    if type(id_equipo) is not int or id_equipo <= 0:
         raise ValueError("valor mayor a cero")

    if not type(id_prestamo) is int or id_prestamo <= 0:
         raise ValueError("valor mayor a cero")

    with Session.begin() as session:
         prestamo = session.get(Prestamo, id_equipo, id_estudiante, id_prestamo)
         if prestamo is None:
              return False

         session.delete(prestamo)