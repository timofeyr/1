import os

class ListModifier:

    def __init__(self, varRange):
        self.range = varRange

    def makeList(self):
        global intList
        intList = []
        for i in range(self.range):
            num = int(input('Enter numbers '))
            intList.append(num)
            i += 0

    def checkForDublicates(self):
        newList = []
        global dublicatesList
        dublicatesList = []
        for num in intList:
            if num not in newList:
                newList.append(num)
            else:
                dublicatesList.append(num)
        if len(dublicatesList) > 0:
            print('This is dublicates: ' + str(dublicatesList))
        else:
            print('There is no dublicates')
    
    def createDublicatesListFile(self):
        try:
            f = open('Dublicates list.txt', 'x')
            f.write('Dublicate(s): ' + str(dublicatesList))
            f.close()
        except FileExistsError:
            if os.path.isfile('Error.txt'):
                os.remove('Error.txt')
                f = open('ErrorNew.txt', 'x')
                f.write('File already exists')
                f.close()
            elif os.path.isfile('ErrorNew.txt'):
                os.remove('ErrorNew.txt')
                f = open('ErrorNew.txt', 'x')
                f.write('File already exists')
                f.close()
            else:
                f = open('Error.txt', 'x')
                f.write('File already exists')
                f.close()
        finally:
            print('\nFile was made')

    def maxListElement(self):
        m = intList[0]
        for i in range(self.range):
            if intList[i] > m:
                m = intList[i]
        print('Max element is ' + str(m))

    def minListElement(self):
        m = intList[0]
        for i in range(self.range):
            if intList[i] < m:
                m = intList[i]
        print('Min element is ' + str(m))

    def showList(self):
        for i in intList:
            print(i, end=' ')