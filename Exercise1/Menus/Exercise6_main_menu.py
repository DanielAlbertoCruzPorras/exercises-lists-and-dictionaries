from Exercise1.Functions.Clear_terminal import clear
from Exercise1.Menus.Exercise3_main_menu import exercise3


def exercise6():
    subjects = []
    grades = []
    subjects2 = []
    grades2 = []
    subjects, grades = exercise3()
    c = 0
    print(f"The passing grade is 64, so you have to repeat the following subjects:")
    for grade in grades: 
      if grade >= 64:
        c += 1
      else:
        subjects2.append(subjects[c])
        grades2.append(grades[c])
        c += 1
    grades = grades2
    subjects = subjects2
    for subject in subjects2:
      print(f"{subject}")
    input("\nPress enter to continue:")
    clear()
