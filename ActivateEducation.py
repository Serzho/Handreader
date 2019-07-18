import Neironet as NN #подключение нейросети 
import numpy as np 
import random


neironet = NN.Neironet() #создание экземпляра нейросети

count_epochs = 200 #количество эпох
count_iterations = 10 #количество интераций

neironet.educateFromBase(count_epochs, count_iterations) #запуск обучения

