import os

# Limpiar la terminal dependiendo del sistema operativo
def clear():
    sistema = os.name  # 'posix' para Linux/Mac y 'nt' para Windows
    if sistema == 'posix':
        os.system('clear')  # Comando para Linux/Mac
    elif sistema == 'nt':
        os.system('cls')    # Comando para Windows