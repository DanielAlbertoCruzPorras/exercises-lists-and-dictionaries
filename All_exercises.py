from Exercise1.Menus.Exercise1_main_menu import exercise1
from Exercise1.Menus.Exercise2_main_menu import exercise2
from Exercise1.Menus.Exercise3_main_menu import exercise3
from Exercise1.Menus.Exercise4_main_menu import exercise4
from Exercise1.Menus.Exercise5_main_menu import exercise5
"""
from Exercise1.Menus.Exercise6_main_menu import exercise6
from Exercise1.Menus.Exercise7_main_menu import exercise7
from Exercise1.Menus.Exercise8_main_menu import exercise8
from Exercise1.Menus.Exercise9_main_menu import exercise9
from Exercise1.Menus.Exercise10_main_menu import exercise10
"""
# Llamamos a la función exercise1() para ejecutar el programa

while True:
        # Mostrar el menú
        print("""\n--- Exercise Menu ---
1. Exercise 1: List of Subjects
2. Exercise 2: Subjects - I study...
3. Exercise 3: Grades in each subject
4. Exercise 4: Lottery Numbers
5. Exercise 5: List of Numbers
0. Salir
""")
        # Solicitar la opción del usuario
        opcion = input("Selecciona un ejercicio (1-10) ó Salir (0): ")

        # HAY QUE CAMBIAR POR MATCH
        if opcion == '1':
            exercise1()
        elif opcion == '2':
            exercise2()
        elif opcion == '3':
            exercise3()
        elif opcion == '4':
            exercise4()
        elif opcion == '5':
            exercise5()
            """
        elif opcion == '6':
            exercise6()
        elif opcion == '7':
            exercise7()
        elif opcion == '8':
            exercise8()
        elif opcion == '9':
            exercise9()
        elif opcion == '10':
            exercise10()"""
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 0 y 3.")

