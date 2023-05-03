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
         yn = input("Покать список, сортированный по дате? y/n ")
         notes_function.list(yn)
         start()
    elif choise == "3":
         number = int(input("Введите номер заметки: "))

         notes_function.read(number)
         start()
    elif choise == "4":
         number= input("Введите номер заметки: ")
         name = input("Введите новое название заметки: ")
         note = input("Введите новый текст заметки: ")
         notes_function.change(number,name,note)
         start()
    elif choise == "5":
         number = input("Введите номер заметки: ")
         notes_function.delete(number)
         start()
    elif choise == "6":
         print("Выход из программы")
         exit()