from Exercise1.Functions.Clear_terminal import clear


def exercise9():
  clear()
  palabra = input("Introduce a word: ").lower()

  vocales = "aeiou"
  conteo_vocales = {vocal: palabra.count(vocal) for vocal in vocales}

  for vocal, conteo in conteo_vocales.items():
      print(f"The vowel '{vocal}' appears {conteo} times.")
  input("\nPress enter to continue:")
  clear()
