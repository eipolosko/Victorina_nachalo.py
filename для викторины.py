from tkinter import *
from tkinter import messagebox

mainWindow = Tk()
mainWindow2 = Tk()

mainWindow.title("Викторина")
mainWindow2.title("Викторина")
mainWindow.geometry("900x900")
mainWindow2.geometry("900x900")


def level_1():  # Метод обработки первого вопроса

    question = Label(mainWindow, text="Какая бывает лопата?", font="Jokerman 20")  # Текст вопроса плюс шрифт текста
    btn1 = Button(mainWindow, text="Совковая", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200", command=lambda: clickCorrectButton())  # Далее создаем кнопки с ответами
    btn2 = Button(mainWindow, text="Граблевая", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200")
    btn3 = Button(mainWindow, text="Тяпковая", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200")
    btn4 = Button(mainWindow, text="Мотыжная", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200")

    def clickCorrectButton():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        level_2()

    question.pack()  # Делаем видимыми элементы,данный метод автоматически выравнивает по центру
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()


def level_2():
    question = Label(mainWindow2, text="Кто такой ара?", font="Jokerman 20")
    btn1 = Button(mainWindow2, text="Дельфин", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200")
    btn2 = Button(mainWindow2, text="Медьведь", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200")
    btn3 = Button(mainWindow2, text="Попугай", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200", command=lambda: clickCorrectButton())
    btn4 = Button(mainWindow2, text="Крокодил", font="Jokerman 20", background="#1E90FF", foreground="#FFFFFF",
                  width="200")

    def clickCorrectButton():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")

    question.pack()
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()


level_1()
mainWindow.mainloop()
mainWindow2.mainloop()