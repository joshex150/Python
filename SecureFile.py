try:
    with open("data.txt") as f_object:
        datas = f_object.read()
    active = True
    admin = ["1060BC",'0000', '1111']
    while active:
        print("-------OPTIONS-------")
        print("1. view all Data")
        print("2. add new Data")
        print("3. add new Admin")
        print("q to quit")
        response = input("Enter an option: ")        
        if response == str(1):
            count = 1
            flag = True
            user = input("Please, what is your Code: ")
            if user in admin:
                print(datas, "\n")                
            else:
                count +=1
                print("Access failed")
                user = input("Please, what is your Code: ")
                if user in admin and count == 2:
                    print(datas, "\n")
                else:
                    count +=1
                    print("Access failed")
                    user = input("Please, what is your Code: ")
                    if user in admin and count == 3:
                        print(datas, "\n")
                    else:
                        count +=1
                        print("Access failed")
                        user = input("This is your last attempt, what is your Code: ")
                        if user in admin and count == 4:
                            print(datas, "\n")
                        else:
                            print("Too many failed attempts you have been blocked")
                            active = False
        elif response == str(2):
            data=input("Enter new Data: ")
            datas+="\n"
            datas+=data
            with open("data.txt", 'w') as f_obj:
                f_obj.write(datas)
                print("New data has been added!")
                active = False
        elif response == str(3):
            pwd= input("Enter admin access password: ")
            if pwd not in admin:
                print("Access Denied!")
            else:
                data=input("Enter new Admin: ")
                admin.append(data)                
        elif response.lower() =="q":
            active = False
        else:
            print("Invalid response!! \n")            
except FileNotFoundError:
    print("seems like you're using this program for the first time")
    proceed = input("would you like to continue? Y/N: ")
    if proceed.lower() != "y":
        exit()
    else:
        with open("data.txt", 'w') as f_obj:
                f_obj.write("")
                print("File created")
    data = ""
    active = True
    with open("data.txt") as f_object:
        datas = f_object.read()
    admin = ["1060BC",'0000', '1111']
    while active:
        print("-------OPTIONS-------")
        print("1. view all Data")
        print("2. add new Data")
        print("3. add new Admin")
        print("q to quit")
        response = input("Enter an option: ")        
        if response == str(1):
            count = 1
            flag = True
            user = input("Please, what is your Code: ")
            if user in admin:
                print(datas, "\n")                
            else:
                count +=1
                print("Access failed")
                user = input("Please, what is your Code: ")
                if user in admin and count == 2:
                    print(datas, "\n")
                else:
                    count +=1
                    print("Access failed")
                    user = input("Please, what is your Code: ")
                    if user in admin and count == 3:
                        print(datas, "\n")
                    else:
                        count +=1
                        print("Access failed")
                        user = input("This is your last attempt, what is your Code: ")
                        if user in admin and count == 4:
                            print(datas, "\n")
                        else:
                            print("Too many failed attempts you have been blocked")
                            active = False
        elif response == str(2):
            data=input("Enter new Data: ")
            datas+="\n"
            datas+=data
            with open("data.txt", 'w') as f_obj:
                f_obj.write(datas)
                print("New data has been added!")
                active = False
        elif response == str(3):
            pwd= input("Enter admin access password: ")
            if pwd not in admin:
                print("Access Denied!")
            else:
                data=input("Enter new Admin: ")
                admin.append(data)
                
        elif response.lower() =="q":
            active = False
        else:
            print("Invalid response!! \n")