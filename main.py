Contact_Book = {}
while True:
    ch = input("To Add press 'a'\nTo Search press 's'\nTo Display press 'd'\nTo Quit press 'q'\n")
    if ch == 'a':
        name = input("Name  :   ")
        phone = input("Phone:   ")
        Contact_Book[name] = phone

    elif ch == 's':
        search = input("what do you want to search? : ")
        print("Mobile Number of ",search, "is", Contact_Book[search])

    elif ch == 'd':
        print(Contact_Book)
        
    else:
        break