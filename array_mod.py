import array_modifier as am

n = int(input('Input range '))

myList = am.ListModifier(n)
myList.makeList()
myList.checkForDublicates()
myList.showList()
myList.createDublicatesListFile()
myList.maxListElement()