from Exercise1.Functions.Clear_terminal import clear
from Exercise1.Functions.Funciones import cargar_asignaturas

def exercise2(): # Main menu
    clear()
    asignaturas = cargar_asignaturas()
    print(f"Yo estudio:\n")
    print(f" ".join(f"{item:>2}" for item in asignaturas))
    input("\nPresione cualquier tecla para continuar:")
    clear()