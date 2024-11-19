from Exercise1.Functions.Clear_terminal import clear
from Exercise1.Functions.Funciones import cargar_asignaturas
from Exercise1.Functions.Funciones import agregar_asignatura
from Exercise1.Functions.Funciones import mostrar_asignaturas
from Exercise1.Functions.Funciones import buscar_asignatura
from Exercise1.Functions.Funciones import borrar_asignatura

"""
Desgloce del ejercicio por funciones y menús
Funciones:
- Agregar asignatura
- Mostrar asignaturas
- Buscar asignatura
- Borrar asignatura
Menús:
Solo el menú principal

-- Menú de opciones ---
1. Agregar asignatura
2. Mostrar asignaturas
3. Buscar asignatura
4. Borrar asignatura
5. Salir
"""

def exercise1(): # Main menu
    clear()
    asignaturas = cargar_asignaturas()
    while True:
        # Menú de opciones
        print("""\n--- Menú de opciones Ejercicio 1 ---
1. Agregar asignatura
2. Mostrar asignaturas
3. Buscar asignatura
4. Borrar asignatura
5. Salir""")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            clear()
            agregar_asignatura(asignaturas)
        elif opcion == '2':
            clear()
            mostrar_asignaturas(asignaturas)
        elif opcion == '3':
            clear()
            buscar_asignatura(asignaturas)
        elif opcion == '4':
            clear()
            borrar_asignatura(asignaturas)
        elif opcion == '5':
            clear()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción entre 1 y 5.")