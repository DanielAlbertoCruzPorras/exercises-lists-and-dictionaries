from Exercise1.Functions.Clear_terminal import clear


def exercise7():
  clear()
  abecedario = list("abcdefghijklmnopqrstuvwxyz")
  # Nota: Las posiciones en Python comienzan en 0
  resultado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0] #enumerate(abecedario) regresa el índice y el item
  print("Resulting list:", resultado)
  input("\nPress enter to continue:")
  clear()
