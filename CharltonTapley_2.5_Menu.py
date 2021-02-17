from os import system
List = ["Cat", "Dog", "Fish"]

def showList():
    for i in List:
        print(i)

def addList(addAnimal):
    List.append(addAnimal)

def deleteList(delAnimal):
    List.remove(delAnimal)

def changeList(addAnimal, delAnimal):
    List.append(addAnimal)
    List.remove(delAnimal)

exit_selected = False
while not exit_selected:
    
    system('cls')  # use 'cls' for windows, 'clear' for Mac
    print('------MENU------')
    print('1 - Show the list')
    print('2 - Add to the list')
    print('3 - Delete from the list')
    print('4 - Change an item in the list')
    print('5 - Sort the list')
    print('0 - Exit')

    print("Currently in the list:", *List, sep=" ")

    selection = input('Enter a number: ')

    system('cls')  # use 'cls' for windows, 'clear' for Mac

    if selection == '1':
        showList()
    elif selection == '2':
        addAnimal = input("Please enter a name of an animal to add to the list: ")
        addList(addAnimal)
    elif selection == '3':
        animal = input("Please enter a name of an animal to delete from the list: ")
        deleteList(delAnimal)
    elif selection == '4':
        delAnimal = input("Please enter the name of an animal to change from the list: ")
        addAnimal = input("Please enter the name of an animal to replace it: ")
        changeList(addAnimal, delAnimal)
    elif selection == '5':
        List.sort()
    elif selection == '0':
        print('Bye!')
        exit_selected = True
        # or you can just use the function exit()
    else:
        print('Please enter a number from the menu')

    input('Press enter to continue')
