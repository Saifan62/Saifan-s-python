import sys
def initial_slambook():
    rows,cols = int(input('Please enter initial number of entries:')),7
    slambook= []
    print(slambook)
    for i in range(rows):
        print("\nEnter entry %d details in the folowing order (ONLY)"%(i+1))
        print("NOTE: * indicates mandatory field")
        print ("..........................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(input("Enter Name* :"))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name cannot be empty. Process terminated.")
            if j == 1:
                temp.append(input("Enter Number* :"))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Number cannot be empty. Process terminated.")
            if j == 2:
                temp.append(input("Enter Hobby* :"))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Hobby cannot be empty. Process terminated.")
            if j == 3:
                temp.append(input("Enter Email address :"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(input("Enter Date of birth:"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 5:
                temp.append(input("Enter favorite game:"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 6:
                temp.append(input("Enter favorite food:"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 7:
                temp.append(input("Enter favorite person:"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
    slambook.append(temp)
    print(slambook)
    return slambook

def menu():
    print("***********************************************")
    print("\t\tSLAMBOOK DIRECTORY")
    print("***********************************************")
    print("\tYou can now perform the following operations on this slambook\n")
    print("1. Add a new entry")
    print("2. Remove an existing entry")
    print("3. Delete all entries")
    print("4. Search for an entry")
    print("5. Display all entries")
    print("6. Exit")

    choice = int(input("Please enter your choice: "))
    return choice
def add_entry(sb):
    temp = []
    for j in range(len(sb[0])):
            if j == 0:
                temp.append(input("Enter Name* :"))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name cannot be empty. Process terminated.")
            if j == 1:
                temp.append(input("Enter Number* :"))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name cannot be empty. Process terminated.")
            if j == 0:
                temp.append(input("Enter Hobby* :"))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Hobby cannot be empty. Process terminated.")
            if j == 0:
                temp.append(input("Enter Email address :"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 0:
                temp.append(input("Enter  favorite food :"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None 
            if j == 0:
                temp.append(input("Enter favorite game :"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 0:
                temp.append(input("Enter favorite person :"))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
    sb.append(temp)
    return sb
def remove_existing(sb):
    query = str (input("Please enter the name of the entry to be rempved:"))
    temp = 0
    for i in range(len(sb)):
        if query == sb[i][0]:
            temp += i
            print(sb.pop(i))
            print("Entry removed successfully.")
            return sb
    if temp == 0:
        print("No entry found with the name:")
        return sb
def delete_all(sb):
        return sb.clear()
def search_entry(sb):
    choice= int(input("Search by:\nName(1)\nHobby(2)\nEmail(3)\nDate of Birth(4)\nFavorite Game(5)\nFavorite Food(6)\nFavorite Person "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Please enter the name of the entry you want to search: "))
        for i in range(len(sb)):
            if query == sb[i][0]:
                temp.append(sb[i])
                check = 1
    elif choice == 2:
        query = str(input("Please enter the hobby of the entry you want to search: "))
        for i in range(len(sb)):
            if query == sb[i][1]:
                temp.append(sb[i])
                check = 1
    elif choice == 3:
        query = str(input("Please enter the Email address of the entry you want to search: "))
        for i in range(len(sb)):
            if query == sb[i][2]:
                temp.append(sb[i])
                check = 1
    elif choice == 4:
        query = str(input("Please enter the favorite game of the entry you want to search: "))
        for i in range(len(sb)):
            if query == sb[i][3]:
                temp.append(sb[i])
                check = 1
    elif choice == 5:
        query = str(input("Please enter the favorite food of the entry you want to search: "))
        for i in range(len(sb)):
            if query == sb[i][4]:
                temp.append(sb[i])
                check = 1
    elif choice == 6:
        query = str(input("Please enter the favorite person of the entry you want to search: "))
        for i in range(len(sb)):
            if query == sb[i][5]:
                temp.append(sb[i])
                check = 1
    else:
        print("Invalid choice. Please try again.")
        return -1
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check
        
def display_all(sb):
    if not sb:
        print("No entries found.")
    else:
        for i in range(len(sb)):
            print(sb[i])
def thanks():
    print("Thank you for using the SlamBook Directory!")
    print("Have a great day!")
    sys.exit()
print("Welcome to the SlamBook Directory!")
ch=1
sb = initial_slambook()
while ch in (1,2,3,4,5,6,7):
    ch = menu()
    if ch == 1:
        sb = add_entry(sb)
    elif ch == 2:
        sb = remove_existing(sb)
    elif ch == 3:
        sb = delete_all(sb)
    elif ch == 4:
        sb = search_entry(sb)
    elif ch == 5:
        display_all(sb)
    elif ch == 6:
        thanks()
    else:
        print("Invalid choice. Please try again.")




        

        


                    



                    
                    

