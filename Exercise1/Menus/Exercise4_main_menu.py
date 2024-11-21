from Exercise1.Functions.Clear_terminal import clear

def exercise4():
    clear()
    numeros = []
    c = 0
    for i in range(6):
        while True:
          try:
              c += 1
              numero = int(input(f"Introduce el número {c} (entre 1 y 49): "))
              if numero < 1 or numero > 49:
                  c -= 1
                  print(f"El número debe estar entre 1 y 49.")
              else:
                  numeros.append(numero)
                  break
          except ValueError:
              print("Por favor, introduce un número válido.")
    numeros = sorted(numeros)
    print(f" ".join(f"{item:>2}" for item in numeros))
    input("\nPresione enter para continuar:")
    clear()