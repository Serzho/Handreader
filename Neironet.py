import numpy as np
from math import *
from tkinter import *
import Base

class Neironet():
    def __init__(self):
        self.base = Base.Base()
    

    def sendField(self, data, mode = 0, letter = -1): #получение данных
        print(data, letter)
        if(mode == 0): #режим тестирования
            print('testing')
            return self.__testing(data) 
        else: #режим обучения
            print('educating')
            return self.__educating(data, letter)


    def __testing(self, data, weights = [], mode = 0): #тестирование 
        sigmoid = lambda x: 1 / (1 + exp(-x)) #функция сигмоида
        
        train_in = [] #создание массива входных данных

        if(mode == 0):
            weights = self.__readWeights()

        if(mode == 0):
            #компановка входных данных
            for i in range(20):
                for k in range(20):
                    train_in.append(data[i][k])
        else:
            train_in = data

        result = round(sigmoid(np.dot(train_in, weights)) * 25 + 65) #получение результата
        print('result', result)
        return result



    def __educating(self, data, letter): #режим обучения       
        train_in = [] #создание массива входных данных
        weights = [] #создание массива синаптических весов
        train_out = ((letter - 65) * 4) / 100 #вычисление выходных данных
        print(train_out)

        #компановка входных данных
        for i in range(20):
            for k in range(20):
                train_in.append(data[i][k])

        weights = self.__readWeights()

        #print(train_in)
        print('before educating', chr(self.__testing(data))) #вывод результата до текущего цикла обучения
        #print('before educating', weights)

        old_weights = weights
        weights = self.__train(train_in, train_out, weights, 8000) #обучение и получение новых весов
         
        self.__saveWeights(weights)

        #self.base.saveToBase(train_in, train_out)
        #print('after educating', weights) 
        print('after educating', chr(self.__testing(data))) #вывод результата после текущего цикла обучения
        print(old_weights == self.__readWeights())

    def educateFromBase(self):
        weights = []
        
        weights = self.__readWeights()

        oldWeights = weights
        
        inputs, outputs = self.base.getBase()
        print(inputs, outputs, len(outputs), weights)
        for k in range(101):
            print('EPOCH: %d' % k)
            for i in range(len(outputs)):
                weights = self.__train(inputs[i], outputs[i], weights, 4000)
            print("RESULTS: ")
            if(k % 10 == 0):
                for i in range(len(outputs)):
                    print('LETTER: %s result %s' % (outputs[i], chr(self.__testing(inputs[i], weights, mode = 1))))

        print(oldWeights == weights)
        
        self.__saveWeights(weights)
        

    def __train(self, t_in, t_out, weights, cycles): #фунция тренировки 
        for i in range(cycles): #повторение обучения
            weights = self.__iteration(t_in, t_out, weights) #обучение и получение новых весов

        return weights

    def __iteration(self, t_in, t_out, weights): #итерация обучения
        sigmoid = lambda x: 1 / (1 + exp(-x)) #функция сигмоида
        x = 0

        for i in range(400): 
            x += weights[i] * t_in[i]
        y = sigmoid(x)

        err = t_out - y #вычисление разницы между нужным и полученным значением
        adjustments  = err * sigmoid(y) 
    
        old_weights = weights
        
        for i in range(400):
            weights[i] += t_in[i] * adjustments #изменение значения для кжаждого веса
        #print(old_weights == weights)

        return weights

    def __readWeights(self):
        weights = []

        #чтение и по необходимости создание файла с синаптическими весами
        try:
            f = open('data', 'r') #пробуем открыть файл        
        except FileNotFoundError: #при отсутствии
            print("New File")

            f = open('data', 'w') #создаем новый файл
            created_weights = 2 * np.random.random(400) - 1 #создаем массив с рандомными весами

            for i in range(400): 
                f.write(str(created_weights[i]) + '\n') #запись массива в файл
                #print(str(created_weights[i]) + '\n')

            f.close() #закрытие файла

            f = open('data', 'r') #пробуем открыть файл еще раз
        finally:
            for line in f.readlines():
                weights.append(float(line.rstrip())) #чтение весов из файла
            f.close() #закрытие файла

        return weights

    def __saveWeights(self, weights):
        #открытие файла и запись новых весов
        f = open('data', 'w') 
        for i in range(400):
                f.write(str(weights[i]) + '\n')
        f.close()



        





