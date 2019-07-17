class Base:
    def __init__(self):
        self.__data = []
        self.__letters = []

    def saveToBase(self, t_in, t_out):
        f = open('base', 'a')
        for i in range(400):
            f.write(str(t_in[i]) + '\n')
        f.write('!' + str(t_out) + '\n')
        f.close()

    def __setBase(self):
        base = []
        f = open('base', 'r')
        for line in f.readlines():
            base.append(line.rstrip()) #чтение весов из файла
        f.close() #закрытие файла

        for b in base:
            if(b[0] == '!'):
                self.__letters.append(float(b[1:]))
            else:
                self.__data.append(float(b))

        array = self.__data
        self.__data = []
        for i in range(len(array) // 400):
            self.__data.append(array[i * 400: (i + 1) * 400])
        print(self.__data, self.__letters, 'CHECKED')

    def getBase(self):
        self.__setBase()
        return self.__data, self.__letters

