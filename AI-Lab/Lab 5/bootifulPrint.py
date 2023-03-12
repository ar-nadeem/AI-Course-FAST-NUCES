class bootifulPrint:
    def __countDigit(self, n):
        count = -1
        if (n < 0):
            n = n * -1
        while n != 0:
            n //= 10
            count += 1
        return count

    def __whatToPrintFirstIndex(self, x):
        if (x < 0):
            print(" "+("―"*(self.__countDigit(x)+4)), end="  ")
        elif (x > 9):
            print(" "+("―"*(self.__countDigit(x)+3)), end="  ")
        else:
            print(" "+"―――", end="  ")

    def __whatToPrint(self, x, e=None):
        if e == None:
            if (x < 0):
                print(" "+("―"*(self.__countDigit(x)+4)), end="  ")
            elif (x > 9):
                print(" "+("―"*(self.__countDigit(x)+3)), end="  ")
            else:
                print(" "+"―――", end="  ")
        else:
            if (x < 0):
                print(" "+("―"*(self.__countDigit(x)+4)), end=e)
            elif (x > 9):
                print(" "+("―"*(self.__countDigit(x)+3)), end=e)
            else:
                print(" "+"―――", end=e)

    def __firstly(self, x):
        for i in range(0, len(x)):
            # FIRST INDEX ONLY
            if (i == 0):
                self.__whatToPrintFirstIndex(x[i])
            ##############################################
            elif (i == len(x)-1):
                self.__whatToPrint(x[i], "\n")
            ##############################################
            else:
                self.__whatToPrint(x[i])
            ################################################

    def __lastly(self, x, e):
        for i in range(0, len(x)):
            # FIRST INDEX ONLY
            if (i == 0):
                self.__whatToPrintFirstIndex(x[i])
            ##############################################
            elif (i == len(x)-1):
                if e != None:
                    self.__whatToPrint(x[i], e)
                else:
                    self.__whatToPrint(x[i], "\n")

            ##############################################
            else:
                self.__whatToPrint(x[i])
            ################################################

    def printArray(self, x, e=None):
        self.__firstly(x)

        for j, i in enumerate(x):
            if (j == len(x)-1):
                print("| "+str(i)+" |", end="\n")
            else:
                print("| "+str(i)+" |", end=" ")

        self.__lastly(x, e)


if __name__ == "__main__":
    arr = [0, 0, 0, 0, 0, 0, 0, 0]
    bPrint = bootifulPrint()
    bPrint.printArray(arr)

    # val = [0, 1, 2, 3, 4, 5, 6, 7]
    # myarr = []
    # a = [0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(8):
    #     a[val.index(i)] = 1
    #     myarr.append(a)
    #     a = [0, 0, 0, 0, 0, 0, 0, 0]

    # print(myarr)
    # for arr in myarr:
    #     bPrint.printArray(arr)
    #     print("\n\n")
