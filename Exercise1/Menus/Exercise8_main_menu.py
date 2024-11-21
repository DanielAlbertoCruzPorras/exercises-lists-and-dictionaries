from Exercise1.Functions.Clear_terminal import clear


def exercise8():
  clear()
  palabra = input("Introduce a word: ").lower()

  if palabra == palabra[::-1]:
      print(f"'{palabra}' is palindrome.")
  else:
      print(f"'{palabra}' isn't palindrome.")
  input("\nPress enter to continue:")
  clear()
