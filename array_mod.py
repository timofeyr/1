import array_modifier as am

n = int(input('Input range '))  #Quantity of numbers

myList = am.ListModifier(n)     #Assign a module to a variable
myList.makeList()               #Makes a list

print('1. Show a list')
print('2. Check, are there any dublicate numbers')
print('3. Make files that contain dublicate numbers')
print('4. Find max element of list')
print('5. Find min element of list')

while True:
    a = int(input('\nWhat do you want? '))

    if a == 1:
        myList.showList()                   #Shows a list  
    elif a == 2:
        myList.checkForDublicates()         #Checks, are there any dublicate numbers 
    elif a ==3:
        myList.createDublicatesListFile()   #Makes files that contain dublicate numbers
    elif a == 4:
        myList.maxListElement()             #Max element of list
    elif a == 4:
        myList.minListElement()             #Min element of list
