import menu
import msvcrt
import notes_function

def start():
    count=0
    choise= menu.menu()
    if choise == "1":
         name = input("Введите название заметки: ")
         note= input("Введите текст заметки: ")
         notes_function.add(name,note)
         start()
    elif choise == "2":
         notes_function.list()
         start()
    elif choise == "3":
         number = input("Введите номер заметки: ")
         notes_function.read(number)
         start()
    elif choise == "4":
         note= input("Введите текст заметки: ")
         notes_function.change(note)
         start()
    elif choise == "5":
         name = input("Введите номер заметки: ")
         notes_function.delete(name)
         start()
    elif choise == "6":
         print("Выход из программы")
         exit()