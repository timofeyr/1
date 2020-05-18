import array_modifier as am

n = int(input('Input range '))      #Quantity of numbers

myList = am.ListModifier(n)         #Assign a module to a variable
myList.makeList()                   #Makes a list
myList.showList()                   #Shows a list    
myList.checkForDublicates()         #Checks, are there any dublicate numbers 
myList.createDublicatesListFile()   #Makes files that contain dublicate numbers
myList.maxListElement()             #Max element of list
