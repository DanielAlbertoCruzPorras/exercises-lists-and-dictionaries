from Exercise1.Functions.Clear_terminal import clear

def exercise5():
    clear()
    numbers = list(range(1, 11))
    i_numbers = numbers[::-1]
    print(f"Original list:\n{numbers}\nInverted list:\n{i_numbers}")
    input("\nPress enter to continue:")
    clear()