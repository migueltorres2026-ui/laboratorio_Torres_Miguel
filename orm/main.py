from sqlalchemy.exc import SQLAlchemyError

from tabla import crear_tabla
from insertar import registrar_Equipo, registrar_Estudiante, registrar_Prestamo
from consulta import consultar_Equipo, consultar_Estudiante, consultar_Prestamo, buscar_Prestamo, buscar_Estudiante, buscar_Equipo
from actualizar import actualizar_Equipo, actualizar_estudiante, actualizar_prestamo
from delete import eliminar_equipo, eliminar_estudiante, eliminar_prestamo


def mostrar_menu():
    print("\n========== SISTEMA DE BIBLIOTECA ==========")
    print("1. Registrar libro")
    print("2. Registrar libro")
    print("3. Registrar libro")
    print("4. Consultar libros")
    print("5. Consultar libros")
    print("6. Consultar libros")
    print("7. Buscar libro por ID")
    print("8. Buscar libro por ID")
    print("9. Buscar libro por ID")
    print("10. Actualizar libro")
    print("11. Actualizar libro")
    print("12. Actualizar libro")
    print("13. Eliminar libro")
    print("14. Eliminar libro")
    print("15. Eliminar libro")
    print("0. Salir")


def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número entero.") from None
    return numero


def pedir_id():
    id_libro = pedir_entero("Ingrese el ID: ")
    if id_libro <= 0:
        raise ValueError("El ID debe ser mayor que cero.")
    return id_libro


def pedir_datos_equipo():
    nombre = input("nombre: ").strip()
    tipo = input("tipor: ").strip()
    stock_disponible = pedir_entero("stock_en_disponibilidad: ")
    return nombre, tipo, stock_disponible
