from tkinter import *
import controller


# def input_inter():   
#     window = Tk()
#     window.title("Добро пожаловать в приложение Телефонный справочник!")
#     window.geometry('1200x800')
#     budy = Label.grid(colum = 4, row = 4)
#     lbl = Label(window, text="Выберите действие", font=("Arial Bold", 24)).grid(column=0, row=0) 
#     window.mainloop()



root = Tk()
root.title("Добро пожаловать в приложение Телефонный справочник!")
root.geometry('1200x800')
Label(text="Имя:", font=("Arial Bold", 24))\
    .grid(row=0, column=0)
Entry(width=70)\
    .grid(row=0, column=1, columnspan=3)
 
Label(text="Столбцов:", font=("Arial Bold", 24))\
    .grid(row=1, column=0)
Spinbox(width=70, from_=1, to=50)\
    .grid(rowspan=2, column=0)
Label(text="Строк:")\
    .grid(row=1, column=2)
Spinbox(width=70, from_=1, to=100)\
    .grid(row=1, column=3)
 
Button(text="Справка").grid(row=2, column=0)
Button(text="Вставить").grid(row=2, column=2)
Button(text="Отменить").grid(row=2, column=3)
 
root.mainloop()