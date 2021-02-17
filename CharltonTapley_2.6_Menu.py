from os import system
Contacts = [{"Name":"Charlton Tapley", "Company": "DMU", "phoneNo": "07766810643", "Email":"Charlton.Tapley@Gmail.com"},
            {"Name":"Isabel Wal", "Company": "NHS", "phoneNo": "07766810123", "Email":"Isabel.Wal@Gmail.com"},
            {"Name":"Harrison Tapley", "Company": "L&W", "phoneNo": "07765345435", "Email":"Harrison.Tapley@Gmail.com"}]

def showList():
    for x in Contacts:
        for key, value in x.items():
            print(key, "=", value)
        print("")

def addContact():
    print("Please enter the following details:  ")
    Name = input("Full name: ")
    Company = input("Company: ")
    phoneNo = input("Phone Number: ")
    Email = input("Email: ")
    addContact = {"Name": Name, "Company": Company, "phoneNo": phoneNo, "Email": Email}
    Contact_copy = addContact.copy()
    Contacts.append(Contact_copy)

def delContact():
    count = 1
    for x in Contacts:
        print(count, x["Name"])
        count += 1
    Number = int(input("What is the number of the contact you would like to remove? "))
    del Contacts[Number-1]

def searchContact():
    Contact = input("Which contact would you like to search for: ")
    Found = False
    for x in Contacts:
        if Contact == (x["Name"]):
            for key, value in x.items():
                print(key, "=", value)
            Found = True
            
    if Found == False:
        print("Contact name not found")

def editContact():
    count = 1
    for x in Contacts:
        print(count, x["Name"])
        count += 1
    Number = int(input("What is the number of the contact you would like to edit? "))
    for key, value in Contacts[Number-1].items():
        print(key, "=", value)
    editVariable = input("Enter the title to overwrite existing data: ")
    userInput = input("Enter text to overwrite existing data: ")

    try:
        Contacts[Number-1].update({editVariable:userInput})
    except:
        print("Invalid input")
    


exit_selected = False
while not exit_selected:
    
    system('cls')  # use 'cls' for windows, 'clear' for Mac
    print('------MENU------')
    print('1 - Show all contacts')
    print('2 - Add a contact')
    print('3 - Delete a contact')
    print('4 - Search a contact')
    print('5 - Sort all contacts')
    print('6 - Edit an existing contact')
    print('0 - Exit')


    selection = input('Enter a number: ')

    system('cls')  # use 'cls' for windows, 'clear' for Mac

    if selection == '1':
        showList()
    elif selection == '2':
        addContact()
    elif selection == '3':
        delContact()
    elif selection == '4':
        searchContact()
    elif selection == '5':
        Contacts.sort( key = lambda i: i['Name'])
    elif selection == '6':
        editContact()
    elif selection == '0':
        print('Bye!')
        exit_selected = True
        # or you can just use the function exit()
    else:
        print('Please enter a number from the menu')

    input('Press enter to continue')