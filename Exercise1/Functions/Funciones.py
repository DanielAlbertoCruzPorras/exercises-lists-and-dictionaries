def agregar_asignatura(asignaturas):
    """Función para agregar una asignatura a la lista si no existe."""
    asignatura = input("Ingrese el nombre de la asignatura: ").strip().upper()
    
    if asignatura in asignaturas:
        print(f"La asignatura '{asignatura}' ya existe en la lista.")
    else:
        asignaturas.append(asignatura)
        print(f"La asignatura '{asignatura}' ha sido añadida.")

def mostrar_asignaturas(asignaturas):
    """Función para mostrar todas las asignaturas."""
    if asignaturas:
        print("Asignaturas actuales:")
        for asignatura in asignaturas:
            print(f"- {asignatura}")
    else:
        print("No hay asignaturas en la lista.")

def buscar_asignatura(asignaturas):
    """Función para buscar una asignatura en la lista."""
    asignatura = input("Ingrese el nombre de la asignatura a buscar: ").strip().upper()
    
    if asignatura in asignaturas:
        print(f"La asignatura '{asignatura}' se encuentra en la lista.")
    else:
        print(f"La asignatura '{asignatura}' no se encuentra en la lista.")
        
def borrar_asignatura(asignaturas):
    """Función para borrar una asignatura de la lista."""
    asignatura = input("Ingrese el nombre de la asignatura a borrar: ").strip().upper()
    
    if asignatura in asignaturas:
        asignaturas.remove(asignatura)
        print(f"La asignatura '{asignatura}' ha sido eliminada.")
    else:
        print(f"La asignatura '{asignatura}' no se encuentra en la lista.")