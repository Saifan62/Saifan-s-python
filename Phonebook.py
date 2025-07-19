import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")),5
    phonebook = []
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY)" % (i + 1))
        print("NOTE : * indicates mandatory field")
        print("....................................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(input("Enter Name* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Name cannot be empty. Process terminated.")
            if j == 1:
                temp.append(input("Enter Number* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Number cannot be empty. Process terminated.")
            if j == 2:
                temp.append(input("Enter Email address : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 3:
                temp.append(input("Enter Date of Birth : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 4:
                temp.append(input("Enter catagory(Family/Friends/Work/Others) : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
        phonebook.append(temp)
    print(phonebook)
    return phonebook

def menu():
      print("***********************************************")
      print("\t\tSMARTPHONE DIRECTORY")
      print("***********************************************")
      print("\tYou can now perform the following operations on this phonebook\n")
      print("1. Add a new contact")
      print("2. Remove an existing contact")
      print("3. Delete all contact")
      print("4. Search for a contact")
      print("5. Display all contacts")
      print("6. Exit")

      choice = int(input("Please enter your choice: "))
      return choice
def add_contact(pb):
        temp = []
        for j in range(len(pb[0])):
            if j == 0:
                temp.append(input("Enter Name* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Name cannot be empty. Process terminated.")
            if j == 1:
                temp.append(input("Enter Number* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Number cannot be empty. Process terminated.")
            if j == 2:
                temp.append(input("Enter Email address : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 3:
                temp.append(input("Enter Date of Birth : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 4:
                temp.append(input("Enter catagory(Family/Friends/Work/Others) : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
                                    
        pb.append(temp)
        return pb
def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you want to remove: ")
    )
    temp = 0
    for i in range(len(pb)):
            if query == pb[i][0]:
                temp += 1
                print(pb.pop(i))
                print("Contact removed successfully.")
                return pb
    if temp == 0:
          print("Sorry, no such contact found.")
          return pb
def delete_all(pb):
      return pb.clear()
def search_existing(pb):
    choice= int(input(" Enter search criteria:\n 1. Name\n 2. Number\n 3. Email\n 4. Date of Birth\n 5. Category\n"))
    temp = []
    check = -1
    if choice == 1:
          query = str(input("Please enter the name of the contact you want to search: "))
          for  i in range(len(pb)):
                if query == pb[i][0]:
                    temp.append(pb[i])
                    check = 1
    elif choice == 2:
          query = str(input("Please enter the number of the contact you want to search: "))
          for  i in range(len(pb)):
                if query == pb[i][1]:
                    temp.append(pb[i])
                    check = 1
    elif choice == 3:
          query = str(input("Please enter the Email address of the contact you want to search: "))
          for  i in range(len(pb)):
                if query == pb[i][2]:
                    temp.append(pb[i])
                    check = 1
    elif choice == 4:
          query = str(input("Please enter the date of birth of the contact you want to search: "))
          for  i in range(len(pb)):
                if query == pb[i][3]:
                    temp.append(pb[i])
                    check = 1
    elif choice == 5:
          query = str(input("Please enter the catagory of the contact you want to search: "))
          for  i in range(len(pb)):
                if query == pb[i][4]:
                    temp.append(pb[i])
                    check = 1
    else:
            print("Invalid choice. Please try again.")
            return -1
    if check == -1:
          return -1
    else:
          display_all(temp)
          return check
def display_all(pb):
      if not pb:
          print("No contacts found.")
      else:
            for i in range(len(pb)):
                  print(pb[i])
def thanks():
    print("Thank you for using the smartphone directory. Goodbye!")
    sys.exit()
print("Welcome to the Smartphone Directory!")
ch= 1
pb = initial_phonebook()
while ch in (1,2,3,4,5):
    ch = menu()
    if ch == 1:
            pb = add_contact(pb)
    elif ch == 2:
            pb = remove_existing(pb)
    elif ch == 3:
            pb = delete_all(pb)
    elif ch == 4:
            search_existing(pb)
    elif ch == 5:
            display_all(pb)
    elif ch == 6:
            thanks()
    else:
            print("Invalid choice. Please try again.")


       
            