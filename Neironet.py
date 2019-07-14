import numpy as np
from math import *
from tkinter import *

class Neironet():
    def __init__(self):
        pass
    

    def sendField(self, data, mode = 0, letter = -1): #получение данных
        if(mode == 0): #режим тестирования
            print('testing')
            return self.__testing(data) 
        else: #режим обучения
            print('educating')
            return self.__educating(data, letter)


    def __testing(self, data): #тестирование 
        sigmoid = lambda x: 1 / (1 + exp(-x)) #функция сигмоида
        weights = [] #создание массива синаптических весов
        train_in = [] #создание массива входных данных

        #чтение весов из файла
        f = open('data', 'r') 
        for line in f.readlines(): 
            weights.append(float(line.rstrip())) 
        f.close()

        #компановка входных данных
        for i in range(10):
            for k in range(10):
                train_in.append(data[i][k])


        result = round(sigmoid(np.dot(train_in, weights)) * 25 + 65) #получение результата 
        print('result', result)
        return result



    def __educating(self, data, letter): #режим обучения       
        train_in = [] #создание массива входных данных
        weights = [] #создание массива синаптических весов
        train_out = ((letter - 65) * 4) / 100 #вычисление выходных данных
        print(train_out)

        #компановка входных данных
        for i in range(10):
            for k in range(10):
                train_in.append(data[i][k])

        #чтение и по необходимости создание файла с синаптическими весами
        try:
            f = open('data', 'r') #пробуем открыть файл        
        except FileNotFoundError: #при отсутствии
            print("New File")

            f = open('data', 'w') #создаем новый файл
            created_weights = 2 * np.random.random(100) - 1 #создаем массив с рандомными весами

            for i in range(100): 
                f.write(str(created_weights[i]) + '\n') #запись массива в файл
                #print(str(created_weights[i]) + '\n')

            f.close() #закрытие файла

            f = open('data', 'r') #пробуем открыть файл еще раз
        finally:
            for line in f.readlines():
                weights.append(float(line.rstrip())) #чтение весов из файла
            f.close() #закрытие файла

        #print(train_in)
        print('before educating', chr(self.__testing(data))) #вывод результата до текущего цикла обучения
        #print('before educating', weights)

        weights = self.__train(train_in, train_out, weights, 20000) #обучение и получение новых весов
             
        #открытие файла и запись новых весов
        f = open('data', 'w') 
        for i in range(100):
                f.write(str(weights[i]) + '\n')
        f.close()

        #print('after educating', weights) 
        print('after educating', chr(self.__testing(data))) #вывод результата после текущего цикла обучения

    def __train(self, t_in, t_out, weights, cycles): #фунция тренировки 
        for i in range(cycles): #повторение обучения
            weights = self.__iteration(t_in, t_out, weights) #обучение и получение новых весов

        return weights

    def __iteration(self, t_in, t_out, weights): #итерация обучения
        sigmoid = lambda x: 1 / (1 + exp(-x)) #функция сигмоида
        x = 0

        for i in range(100): 
            x += weights[i] * t_in[i]
        y = sigmoid(x)

        err = t_out - y #вычисление разницы между нужным и полученным значением
        adjustments  = err * sigmoid(y) 
        
        for i in range(100):
            weights[i] += t_in[i] * adjustments #изменение значения для кжаждого веса

        return weights
            





