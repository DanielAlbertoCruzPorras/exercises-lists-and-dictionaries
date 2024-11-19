from Exercise1.Menus.Exercise1_main_menu import exercise1
from Exercise1.Menus.Exercise2_main_menu import exercise2
# Llamamos a la función exercise1() para ejecutar el programa

while True:
        # Mostrar el menú
        print("\n--- Menú de Ejercicios ---")
        print("1. Ejercicio 1: Lista de Asignaturas")
        print("2. Ejercicio 2: Asignaturas - Yo estudio...")
        print("0. Salir")

        # Solicitar la opción del usuario
        opcion = input("Selecciona un ejercicio (0-3): ")

        # Ejecutar el ejercicio correspondiente
        if opcion == '1':
            exercise1()
        elif opcion == '2':
            exercise2()
        elif opcion == '3':
             print("""
========================
  Opcion en desarrollo
========================""")
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 0 y 3.")

