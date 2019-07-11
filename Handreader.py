#подключение стандартный библиотек
import sys 

#подключение сторонних библиотек
import threading as th

#подключение своих модулей
import UserInterface as UI #подключение пользовательского интерфейса
import Neironet as NN         

learning = True #запускать ли с режимом обучения

if(len(sys.argv) == 2): #проверка на дополнительный аргумент при запуске
    #определеине аргумента
    if(sys.argv[1] == '-l'): #аргумент для обучения
        learning = True #включение режима обучения

neironet = NN.Neironet() #создание экземпляра нейросети
userInterface = UI.UserInterface(learning, neironet) #создание экземпляра класса GUI и передача аргументов



