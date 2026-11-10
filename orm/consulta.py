from sqlalchemy import select
from conexion import Session
from  modelo import Equipo, Estudiante, Prestamo

def consultar_Equipo():
    with Session() as session:
        consulta = select(Equipo).order_by(Equipo.id)
        equipos = session.scalars(consulta).all()

        return equipos

def consultar_Estudiante():
    with Session() as session:
        consulta = select(Estudiante).order_by(Estudiante.id)
        estudiantes = session.scalars(consulta).all()

        return estudiantes

def consultar_Prestamo():
    with Session() as session:
        consulta = select(Prestamo).order_by(Prestamo.id)
        prestamos = session.scalars(consulta).all()

        return prestamos

def buscar_Equipo(id_equipo):
    if type(id_equipo) is not int or id_equipo <= 0:
        raise ValueError("ID invalido")

    with Session() as session:
        equipo = session.get(Equipo, id_equipo)
        return equipo


def buscar_Estudiante(id_estudiante):
    if type(id_estudiante) is not int or id_estudiante <= 0:
        raise ValueError("ID invalido")

    with Session() as session:
        estudiante = session.get(Equipo, id_estudiante)
        return estudiante

def buscar_Prestamo(id_prestamo):
    if type(id_prestamo) is not int or id_prestamo <= 0:
        raise ValueError("ID invalido")

    with Session() as session:
        prestamo = session.get(Equipo, id_prestamo)
        return prestamo



