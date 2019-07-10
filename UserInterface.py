#импорт стандартных библиотек
from tkinter import * #импорт сатндартной библиотеки GUI

class UserInterface(): #класс пользовательского интерфейса
    def __init__(self, learning = False): #функция инициализации
        #присваивание значений атрибутов
        self.__learning = learning #режим обучение

        #создание окна
        self.__window = Tk() #объект окна
        self.__window.title("Handreader") #создание заголовка окна
        self.__window.geometry('600x480') #задаем размер окна
        self.__window.resizable(0, 0) #фиксируем размеры окна

        #создание элементов окна
        #создаем поле для рисования
        self.__canvas = Canvas(self.__window, width = 250, height = 250, bg = "white") #создание поля рисования
        self.__canvas.pack() #упаковываем поле
        self.__canvas.bind("<B1-Motion>", self.__drawCanvas) #привязываем событие зажатой кнопки к функции рисования
        self.__canvas.place(x = 275, y = 50) #выставление координат 

        #создание кнопок
        self.__inputBtn = Button(self.__window, text = "Ок", command = self.__input, width = 10) #создание кнопки OK
        self.__inputBtn.place(x = 50, y = 100) #выставление координат 

        self.__clearBtn = Button(self.__window, text = "Очистить", command = self.__clearCanvas, width = 10) #создание кнопки ОЧИСТИТЬ
        self.__clearBtn.place(x = 50, y = 140) #выставление координат 

        if(learning): #создание элементов для разработчика
            self.__selectLetters = Entry(self.__window, width = 5) #создание текствого поля для ввода буквы
            self.__selectLetters.place(x = 50, y = 340) #выставление координат

            self.__acceptLetter = Button(self.__window, text = "Ок", command = self.__acceptLetter) #создание кнопки 
            self.__acceptLetter.place(x = 90, y = 340) #выставление координат

            self.__selectTesting = Radiobutton(self.__window,text = "Тестирование", 
                                               value = 1, command = self.__testing) #создание кнопки выбора тестирования
            self.__selectTesting.place(x = 50, y = 240) #выставление координат
            self.__selectEducation = Radiobutton(self.__window, text = "Обучение",
                                                value = 2, command = self.__education) #создание кнопки выбора обучения
            self.__selectEducation.place(x = 50, y = 280) #выставление координат

        self.__window.mainloop() #запуск цикла окна 


    def __acceptLetter(self): #функция ввода буквы на обучение
        pass

    def __testing(self): #функция для выбора режима тестирования
        self.__selectLetters.place_forget() #удаление текстового поля
        self.__acceptLetter.place_forget() #удаление кнопки для подтверждения буквы

    def __education(self): #функция для выбора режима обучения
        self.__selectLetters.place(x = 50, y = 340) #возвращение текстового поля 
        self.__acceptLetter.place(x = 90, y = 340) #возварщение кнопки для подтверждения буквы

    def __input(self): #функция ввода прописной буквы
        pass

    def __drawCanvas(self, event): #функция рисования на поле
        self.__canvas.create_oval(event.x - 1, event.y - 1, #создаем круг по координате мышки с радиусом 1
                                 event.x + 1, event.y + 1,
                                 fill = "black") #заливаем круг черным цветом

    def __clearCanvas(self): #функция очистки поля
        self.__canvas.delete("all")

