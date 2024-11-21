from Exercise1.Functions.Clear_terminal import clear
from Exercise1.Functions.Funciones import cargar_asignaturas


def exercise3():
    clear()
    grade = []
    c = 0
    asignaturas = cargar_asignaturas()
    while True:
        try:
            for asignatura in asignaturas:
                grade.append(float(input(f"Cuál fué su nota en {asignatura}?\n")))
                clear()
            break
        except ValueError:
            print("Entrada inválida, inténtelo de nuevo")
            grade.clear()
    clear()
    for item in asignaturas:
        print(f"En {item} has sacado {grade[c]}")
        c += 1
    input("\nPresione enter para continuar")
    clear()
    return asignaturas, grade