from Exercise1.Functions.Clear_terminal import clear

def exercise1(): # Main menu
    asignaturas = []
    
    while True:
        # Menú de opciones
        print("\n--- Menú de opciones ---")
        print("1. Agregar asignatura")
        print("2. Mostrar asignaturas")
        print("3. Buscar asignatura")
        print("4. Borrar asignatura")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            clear()
            print("""========================
  Opción en desarrollo
========================""")
            #agregar_asignatura(asignaturas)
        elif opcion == '2':
            clear()
            print("""========================
  Opción en desarrollo
========================""")
            #mostrar_asignaturas(asignaturas)
        elif opcion == '3':
            clear()
            print("""========================
  Opción en desarrollo
========================""")
            #buscar_asignatura(asignaturas)
        elif opcion == '4':
            clear()
            print("""========================
  Opción en desarrollo
========================""")
            #borrar_asignatura(asignaturas)
        elif opcion == '5':
            clear()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción entre 1 y 5.")