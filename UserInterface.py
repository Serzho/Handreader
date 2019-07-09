#импорт стандартных библиотек
from tkinter import * #импорт сатндартной библиотеки GUI

class UserInterface():
    def __init__(self, learning = False):
        #присваивание значений атрибутов
        self.__learning = learning #режим обучение
        #создание окна
        self.__window = Tk() #объект окна
        self.__window.title("Handreader") #создание заголовка окна
        self.__window.mainloop() #запуск цикла окна
