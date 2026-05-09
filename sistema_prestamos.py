# =============================================================================
# Sistema de Préstamos de Equipos
# Aplicación para gestionar inventario, préstamos y devoluciones de equipos
# Conceptos aplicados: listas, tuplas, diccionarios y funciones modulares
# =============================================================================

from datetime import date

# -----------------------------------------------------------------------------
# INVENTARIO INICIAL
# Diccionario anidado: clave = nombre del equipo
#   "disponible" (bool)  → True si está libre, False si está prestado
#   "prestamos"  (list)  → lista de tuplas (usuario, fecha) — inmutables
# -----------------------------------------------------------------------------
equipos = {
    "Laptop Dell": {
        "disponible": True,
        "prestamos": []
    },
    "Laptop HP": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Samsung": {
        "disponible": True,
        "prestamos": []
    },
    "Proyector Epson": {
        "disponible": True,
        "prestamos": []
    },
    "PC de Escritorio": {
        "disponible": False,
        "prestamos": [("Carlos Pérez", "2025-04-20")]  # Préstamo de ejemplo
    }
}


# =============================================================================
# FUNCIÓN 1: Mostrar equipos
# =============================================================================
def mostrar_equipos():
    """Muestra todos los equipos con su estado actual (disponible / prestado)."""
    print("\n" + "=" * 50)
    print("INVENTARIO DE EQUIPOS")
    print("=" * 50)

    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"  • {nombre:<22} → {estado}")

    print("=" * 50)


# =============================================================================
# FUNCIÓN 2: Registrar préstamo
# =============================================================================
def registrar_prestamo():
    """Registra un nuevo préstamo asociando el equipo a un usuario y fecha."""
    print("\n" + "=" * 50)
    print("REGISTRAR PRÉSTAMO")
    print("=" * 50)

    # Mostrar solo los equipos disponibles
    disponibles = [nombre for nombre, datos in equipos.items() if datos["disponible"]]

    if not disponibles:
        print("No hay equipos disponibles en este momento.")
        return

    print("  Equipos disponibles:")
    for nombre in disponibles:
        print(f"    • {nombre}")

    # Solicitar el nombre del equipo
    equipo_elegido = input("\n  Ingresa el nombre exacto del equipo a prestar: ").strip()

    # Validar que el equipo exista
    if equipo_elegido not in equipos:
        print(f"El equipo '{equipo_elegido}' no existe en el sistema.")
        return

    # Validar que el equipo esté disponible
    if not equipos[equipo_elegido]["disponible"]:
        print(f" El equipo '{equipo_elegido}' ya está prestado.")
        return

    # Solicitar el nombre del usuario
    usuario = input("  Ingresa el nombre del usuario que hace el préstamo: ").strip()
    if not usuario:
        print("El nombre del usuario no puede estar vacío.")
        return

    # Registrar el préstamo como tupla inmutable (usuario, fecha)
    fecha_hoy = str(date.today())           # Fecha actual en formato YYYY-MM-DD
    registro = (usuario, fecha_hoy)         # Tupla inmutable

    equipos[equipo_elegido]["prestamos"].append(registro)   # Añadir al historial
    equipos[equipo_elegido]["disponible"] = False            # Marcar como no disponible

    print(f"\n Préstamo registrado exitosamente:")
    print(f"     Equipo  : {equipo_elegido}")
    print(f"     Usuario : {usuario}")
    print(f"     Fecha   : {fecha_hoy}")


# =============================================================================
# FUNCIÓN 3: Devolver equipo
# =============================================================================
def devolver_equipo():
    """Marca un equipo como devuelto y lo deja disponible nuevamente."""
    print("\n" + "=" * 50)
    print("DEVOLVER EQUIPO")
    print("=" * 50)

    # Mostrar los equipos actualmente prestados
    prestados = [nombre for nombre, datos in equipos.items() if not datos["disponible"]]

    if not prestados:
        print("No hay equipos prestados actualmente.")
        return

    print("  Equipos actualmente prestados:")
    for nombre in prestados:
        print(f"    • {nombre}")

    # Solicitar el nombre del equipo a devolver
    equipo_elegido = input("\n  Ingresa el nombre exacto del equipo a devolver: ").strip()

    # Validar que el equipo exista
    if equipo_elegido not in equipos:
        print(f" El equipo '{equipo_elegido}' no existe en el sistema.")
        return

    # Validar que el equipo esté prestado
    if equipos[equipo_elegido]["disponible"]:
        print(f" El equipo '{equipo_elegido}' ya está disponible en el inventario.")
        return

    # Marcar como disponible nuevamente
    equipos[equipo_elegido]["disponible"] = True
    print(f"\n El equipo '{equipo_elegido}' ha sido devuelto y está disponible.")


# =============================================================================
# FUNCIÓN 4: Ver historial de préstamos
# =============================================================================
def ver_historial():
    """Muestra el historial completo de préstamos de todos los equipos."""
    print("\n" + "=" * 50)
    print("HISTORIAL DE PRÉSTAMOS")
    print("=" * 50)

    for nombre, datos in equipos.items():
        print(f"\n {nombre}:")

        # Verificar si el equipo tiene préstamos registrados
        if not datos["prestamos"]:
            print("       Sin préstamos registrados.")
        else:
            # Recorrer la lista de tuplas (usuario, fecha)
            for i, (usuario, fecha) in enumerate(datos["prestamos"], start=1):
                print(f"       {i}. Usuario: {usuario:<20} | Fecha: {fecha}")

    print("\n" + "=" * 50)


# =============================================================================
# FUNCIÓN 5: Agregar nuevo equipo
# =============================================================================
def agregar_equipo():
    """Agrega un nuevo equipo al inventario con estado disponible y sin préstamos."""
    print("\n" + "=" * 50)
    print("AGREGAR NUEVO EQUIPO")
    print("=" * 50)

    nuevo_equipo = input("  Ingresa el nombre del nuevo equipo: ").strip()

    if not nuevo_equipo:
        print(" El nombre del equipo no puede estar vacío.")
        return

    # Verificar que el equipo no exista ya en el diccionario
    if nuevo_equipo in equipos:
        print(f" El equipo '{nuevo_equipo}' ya está registrado en el sistema.")
        return

    # Agregar el nuevo equipo con estado disponible y lista de préstamos vacía
    equipos[nuevo_equipo] = {
        "disponible": True,
        "prestamos": []
    }

    print(f"\n Equipo '{nuevo_equipo}' agregado exitosamente al inventario.")


# =============================================================================
# FUNCIÓN PRINCIPAL: Menú interactivo
# =============================================================================
def menu():
    """Muestra el menú principal y gestiona la navegación entre opciones."""

    opciones_validas = {"1", "2", "3", "4", "5", "6"}

    while True:
        # Mostrar el menú
        print("\n" + "=" * 50)
        print(" SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("=" * 50)
        print("  1. Ver inventario de equipos")
        print("  2. Registrar préstamo")
        print("  3. Devolver equipo")
        print("  4. Ver historial de préstamos")
        print("  5. Agregar nuevo equipo")
        print("  6. Salir")
        print("=" * 50)

        opcion = input("  Selecciona una opción (1-6): ").strip()

        # Validar opción ingresada
        if opcion not in opciones_validas:
            print(" Opción no válida. Por favor elige entre 1 y 6.")
            continue

        # Llamar a la función correspondiente
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("\n Saliendo del sistema. ¡Hasta luego!\n")
            break


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    menu()