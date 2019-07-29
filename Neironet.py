#импорт стандартных библиотек
from math import *
from tkinter import *

#импорт сторонних библиотек
import numpy as np

#импорт своих модулей
import BaseControl

class Neironet():
    def __init__(self): #инициализация
        self.baseControl = BaseControl.BaseControl() #экзмпляр класса управления базой
    

    def sendField(self, data, mode = 0, letter = -1): #получение данных
        #print(data, letter)
        if(mode == 0): #режим тестирования
            print('testing')
            return self.__testing(data)  
        else: #режим обучения
            print('educating')
            return self.__educating(data, letter)


    def __testing(self, data, weights = [], mode = 0): #тестирование 
        sigmoid = lambda x: 1 / (1 + exp(-x)) #функция сигмоида
        
        train_in = [] #создание массива входных данных
        tests = [] #создание массива результатов для проверки на всех буквах

        if(mode == 0): #
            weights = self.__readWeights() #чтение весов, если те не были переданы в качестве параметра

            #компановка входных данных
            for i in range(20):
                for k in range(20):
                    train_in.append(data[i][k])
        else:
            train_in = data 

        for weight in weights: #проверка на всех буквах 
            tests.append(sigmoid(np.dot(train_in, weight))) #получение результата

        probablity = max(tests) #нахождение максимальной вероятности
        result = tests.index(probablity) + 65 #нахождение буквы с максимальной вероятностью
        probablity_of_success = (probablity / sum(tests)) #нахождение вероятности успешности полученной результата
        print('result %s probablity %f %s' % (chr(result), probablity_of_success, chr(10084))) #вывод результата, вероятности и сердешка <3
        if(probablity_of_success < 0.6):
            result = ord('?')
        return result

    def __educating(self, data, letter): #режим обучения       
        train_in = [] #создание массива входных данных
        weights = [] #создание массива синаптических весов
        train_out = letter - 65 #вычисление выходных данных
        #print(train_out)

        #компановка входных данных
        for i in range(20):
            for k in range(20):
                train_in.append(data[i][k])

        weights = self.__readWeights() #чтение весов

        #print('weights ', weights)
        #print(train_in)
        print('before educating', chr(self.__testing(data))) #вывод результата до текущего цикла обучения

        weights = self.__train(train_in, train_out, weights, 10) #обучение и получение новых весов
         
        self.__saveWeights(weights) #сохранение новых весов

        self.baseControl.saveToBase(train_in, train_out) #сохранение входных и выходных данных
        #print('after educating', weights) 
        print('after educating', chr(self.__testing(data))) #вывод результата после текущего цикла обучения

    def educateFromBase(self, count_Epochs, count_Iterations): #обучение из базы дыннах
        check = lambda o, i, w: self.__intermediateResult(o, i, w) #проверка для всех входных данных
        weights = self.__readWeights() #чтение весов
        
        inputs, outputs = self.baseControl.getBase() #получение входных и выходных данных из базы данных
        #print(inputs, outputs, len(outputs), weights)
        for k in range(count_Epochs): #тренировка по эпохам
            print('EPOCH: %d' % k) #вывод текущих эпох
            for i in range(len(outputs)): #обучение по всем входным и выходным данным
                weights = self.__train(inputs[i], outputs[i], weights, count_Iterations) #обучение и получение новых весов
            
            if((k % (count_Epochs//4)) == 0): #промежуточный результат 4 раза за обучение
                check(outputs, inputs, weights) #проверка для всех входных данных
            
        print('TOTAL' * 10) #конечынй результат
        check(outputs, inputs, weights) #проверка для всех входных данных
        #print(oldWeights == weights)
        
        self.__saveWeights(weights)
        
    def __intermediateResult(self, outputs, inputs, weights): #проверка для всех букв
        print("RESULTS: ")
        for i in range(len(outputs)): #проход по всем данным
            print('LETTER: %s result %s' % (outputs[i], chr(self.__testing(inputs[i], weights, mode = 1)))) #вывод результата

    def __train(self, t_in, t_out, weights, cycles): #фунция тренировки 
        for i in range(cycles): #повторение обучения
            weights = self.__iteration(t_in, t_out, weights) #обучение и получение новых весов

        return weights 

    def __iteration(self, t_in, out, weights): #итерация обучения
        sigmoid = lambda x: 1 / (1 + exp(-x)) #функция сигмоида
        t_out = np.zeros(26) #создание массива со всеми нулями
        t_out[int(out)] = 1 #присваивание еденицы элементу с индексом равным верному результату

        #print('letter: ', out, 'array', t_out)
        #print('count of weights: %d' % len(weights))

        for i in range(26): #проход по всем буквам 
            layer0 = np.array(t_in) #слой с входными данными
            layer1 = sigmoid(np.dot(layer0, weights[i])) #скрытый слой

            err = t_out[i] - layer1 #вычисление разницы между нужным и полученным значением
            adjustments  = err * sigmoid(layer1) * 0.05 #вычисления значений для добавления к первоначальным весам
            
            weights[i] += np.dot(layer0.T, adjustments) #изменение значения для каждого веса

        return weights

    def __readWeights(self): #чтение весов из файла
        weights = [] #создание массива весамов
        data = [] #создание временного массива

        #чтение и по необходимости создание файла с синаптическими весами
        try:
            f = open('data', 'r') #пробуем открыть файл        
        except FileNotFoundError: #при отсутствии
            self.__createWeights()
            f = open('data', 'r') #пробуем открыть файл еще раз
        finally:
            for line in f.readlines():
                data.append(float(line.rstrip())) #чтение весов из файла
            f.close() #закрытие файла

        for i in range(len(data) // 400): #компановка весов по 400 для каждой буквы
            weights.append(data[i * 400: (i + 1) * 400]) #добавление весов

        return weights

    def __createWeights(self): #создание весов
        print("New File")
        np.random.seed(1) 
        f = open('data', 'w') #создаем новый файл
        created_weights = 2 * np.random.random((26, 400)) - 1 #создаем массив с рандомными весами

        for letter in created_weights: #проход по весам для каждой буквы
            for i in range(400): #проход по всем весам конкретной буквы
                f.write(str(letter[i]) + '\n') #запись массива в файл
                #print(str(created_weights[i]) + '\n')

        f.close() #закрытие файла


    def __saveWeights(self, weights): #сохранение весов
        #открытие файла и запись новых весов
        f = open('data', 'w')  
        for letter in weights:
            for i in range(400):
                f.write(str(letter[i]) + '\n')

        f.close()



        





