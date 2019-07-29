#импорт стандартных библиотек
from tkinter import * #импорт сатндартной библиотеки GUI
from tkinter import messagebox  

#импорт сторонних библиотек
import numpy as np #импорт numpy

#подключение своих модулей
import Neironet as NN #подключение нейросети

class UserInterface(): #класс пользовательского интерфейса
    def __init__(self, learning = False, neironet = None): #функция инициализации
        #присваивание значений атрибутов
        self.__teachLetter = -1
        self.__neironet = neironet #нейросеть
        self.__learning = learning #режим обучение
        self.__field = np.zeros((20, 20)) #значения для передачи письменной буквы 
        self.__mode = 0 #режим 0 (тестирование)..... 1 (обучение) 

        #создание окна
        self.__window = Tk() #объект окна
        self.__window.title("Handreader") #создание заголовка окна
        self.__window.geometry('600x480') #задаем размер окна
        self.__window.resizable(0, 0) #фиксируем размеры окна

        #создание элементов окна
        #создание поля для рисования
        self.__canvas = Canvas(self.__window, width = 200, height = 200, bg = "white") #создание поля рисования
        self.__canvas.pack() #упаковка поля
        self.__canvas.bind("<B1-Motion>", self.__drawCanvas) #привязывание события зажатой кнопки к функции рисования
        self.__canvas.place(x = 275, y = 50) #выставление координат 

        #создание поля для отображения передаваемых значений
        self.__outputCanvas = Canvas(self.__window, width = 60, height = 60, bg = "white") #создание поля
        self.__outputCanvas.pack() #упаковка поля
        self.__outputCanvas.place(x = 375, y = 315) #выставление координат

        #создание кнопок
        self.__inputBtn = Button(self.__window, text = "Ок", command = self.__input, width = 10) #создание кнопки OK
        self.__inputBtn.place(x = 50, y = 100) #выставление координат 

        self.__clearBtn = Button(self.__window, text = "Очистить", command = self.__clearCanvas, width = 10) #создание кнопки ОЧИСТИТЬ
        self.__clearBtn.place(x = 50, y = 140) #выставление координат 

        if(learning): #создание элементов для разработчика
            self.__selected = IntVar()
            
            self.__selectLetters = Entry(self.__window, width = 5) #создание текствого поля для ввода буквы
            self.__selectLetters.place(x = 50, y = 340) #выставление координат

            self.__acceptLetter = Button(self.__window, text = "Ок", command = self.__acceptLetter) #создание кнопки 
            self.__acceptLetter.place(x = 90, y = 340) #выставление координат

            self.__selectTesting = Radiobutton(self.__window,text = "Тестирование", 
                                               value = 1, command = self.__testing, variable = self.__selected) #создание кнопки выбора тестирования
            self.__selectTesting.place(x = 50, y = 240) #выставление координат
            self.__selectEducation = Radiobutton(self.__window, text = "Обучение",
                                                value = 2, command = self.__education, variable = self.__selected) #создание кнопки выбора обучения
            self.__selectEducation.place(x = 50, y = 280) #выставление координат

        self.__window.mainloop() #запуск цикла окна

    def __acceptLetter(self): #функция ввода буквы на обучение
        self.__teachLetter = ord(self.__selectLetters.get())     

    def __testing(self): #функция для выбора режима тестирования
        self.__mode = 0
        self.__selectLetters.place_forget() #удаление текстового поля
        self.__acceptLetter.place_forget() #удаление кнопки для подтверждения буквы

    def __education(self): #функция для выбора режима обучения
        self.__mode = 1
        self.__selectLetters.place(x = 50, y = 340) #возвращение текстового поля 
        self.__acceptLetter.place(x = 90, y = 340) #возварщение кнопки для подтверждения буквы

    def __input(self): #функция ввода прописной буквы
        self.__outputCanvas.delete("all") #очистка дополнительного поля
        #отрисовка данных для отправки на доп поле
        for i in range(20): 
            for k in range(20):
                if(bool(self.__field[i][k])):
                         self.__outputCanvas.create_oval(i * 3, k * 3, i * 3 + 3, k * 3 + 3)
        self.__sendField()
                    

    def __drawCanvas(self, event): #функция рисования на поле
        self.__canvas.create_oval(event.x - 1, event.y - 1, #создаем круг по координате мышки с радиусом 1
                                 event.x + 1, event.y + 1,
                                 fill = "black") #заливаем круг черным цветом
        #безопасный код для добавления данных на отправку
        try: 
            self.__field[round(event.x/10), round(event.y/10)] = 1
        except IndexError: #исключение при выходе мыши за поле для рисования
            print("Out of field")

    def __clearCanvas(self): #функция очистки полей
        self.__canvas.delete("all") #очистка главного поля
        
    def __clearField(self):
        #очистка данных на отправку
        for i in range(20):
            for k in range(20):
                self.__field[i][k] = 0

    def __sendField(self): #функция передачи данных
        self.__clearCanvas() #очистка поля
        output = self.__neironet.sendField(data = self.__field, mode = self.__mode, letter = self.__teachLetter) #отправка данных и получение ответа от нейросети 
        self.__clearField() #очистка данных

        if(not(output is None)): #если получен ответ (режим тестирования)
            messagebox.showinfo('Результат:', chr(output)) #вывод окна с результатом
        
        




