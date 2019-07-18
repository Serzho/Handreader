class BaseControl: #класс контроллера базы
    def __init__(self): #инициализация
        self.__data = [] #созданние массива входных данных 
        self.__letters = [] #создание массивы выходных данных

    def saveToBase(self, t_in, t_out): #сохранение в базу
        f = open('base', 'a')
        for i in range(400):
            f.write(str(t_in[i]) + '\n')
        f.write('!' + str(t_out) + '\n')
        f.close()

    def __setBase(self): #получение базы из файла
        base = []
        f = open('base', 'r')
        for line in f.readlines():
            base.append(line.rstrip()) #чтение данных из файла
        f.close() #закрытие файла

        #распределения входных и выходных данных
        for b in base: 
            if(b[0] == '!'):
                self.__letters.append(float(b[1:]))
            else:
                self.__data.append(float(b))

        #компановка данных
        array = self.__data
        self.__data = []
        for i in range(len(array) // 400):
            self.__data.append(array[i * 400: (i + 1) * 400])
        print(self.__data, self.__letters, 'CHECKED')

    def getBase(self): #возвращение базы
        self.__setBase()
        return self.__data, self.__letters

