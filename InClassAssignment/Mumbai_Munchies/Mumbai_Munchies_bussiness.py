import json

# Global variables for file paths
STAFF_CREDENTIALS_FILE = "staff_credentials.json"
SNACK_LIST_FILE = "Snack_list.json"

# Initialize Snack_List and Snack_order lists
Snack_List = []
Snack_order = []

# Function to display the initial greeting and user/staff selection
def greet():
    print("======================================\n")
    print("Welcome to Mumbai Munchies!")
    print("======================================\n")
    user_or_staff()

# Function for staff registration
def staff_registration():
    load_staff_data()
    
    username = input("Enter a username for registration: ")
    password = input("Enter a password for registration: ")

    staff_data = {
        "role": "staff",
        "username": username,
        "password": password
    }
    
    Snack_List.append(staff_data)
    save_staff_data()
    print("Staff registered successfully!")
    staff_login()

# Function for staff login
def staff_login():
    load_staff_data()

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    staff_data = None
    for user in Snack_List:
        if user.get("role") == "staff" and user.get("username") == username and user.get("password") == password:
            staff_data = user
            break
    
    if staff_data:
        start()
    else:
        print("Invalid credentials. Please try again.")
        ifWantToRegister = input("You want to register as a staff member? (y/n): ")
        if ifWantToRegister == "y":
            staff_registration()
        else:
            user_or_staff()

# Function to display user/staff selection
def user_or_staff():
    print("Please choose an option:")
    print("1) User")
    print("2) Staff")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        user_menu()
    elif choice == "2":
        staff_login()
    else:
        print("Invalid choice. Please select again.")
        user_or_staff()

# Function to display user menu
def user_menu():
    print("Welcome to the user!")

# Function to save staff data to file
def save_staff_data():
    with open(STAFF_CREDENTIALS_FILE, "w") as file:
        json.dump(Snack_List, file)

# Function to load staff data from file
def load_staff_data():
    global Snack_List
    try:
        with open(STAFF_CREDENTIALS_FILE, "r") as file:
            Snack_List = json.load(file)
    except FileNotFoundError:
        Snack_List = []

# Function to save snack data to file
def save_data():
    with open(SNACK_LIST_FILE, "w") as file:
        json.dump(Snack_List, file)

# Function to load snack data from file
def load_data():
    global Snack_List
    try:
        with open(SNACK_LIST_FILE, "r") as file:
            Snack_List = json.load(file)
    except FileNotFoundError:
        Snack_List = []

# Function to start the main program loop
def start():
    load_data()
    print("======================================\n")
    print("Welcome to Mumbai Munchies!")
    print("1) Add Snack to Munchies.")
    print("2) Show the Menu.")
    print("3) Update the Snack.")
    print("4) Delete the Snack from munchies.")
    print("5) Exit the program.")
    print("6) Order a Snack from munchies (By id).")
    print("======================================\n")

    try:
        choosed_option = int(
            input("Enter the task no you wanted to do from above list: "))
        if choosed_option == 1:
            Add_Snack()
        elif choosed_option == 2:
            ShowSnack()
        elif choosed_option == 3:
            updateSnack()
        elif choosed_option == 4:
            DeleteSnack()
        elif choosed_option == 5:
            ExitTheProgramme()
    except ValueError:
        print("Please `Enter the valid Input!!")

# Function to exit the program
def ExitTheProgramme():
    print("See you again ❤ ❤")

# Function to delete a snack
def DeleteSnack():
    id_of_snack = int(input("Enter the Snack Id you want to Delete: "))
    snack = None
    for i in Snack_List:
        if i["id"] == id_of_snack:
            snack = i
            break
        
    if snack is None:
        print("Snack not found. Please enter a valid Snack ID.")
    else:
        decision_to_delete = input("Are you sure you want to delete this snack? (y/n): ")
        if decision_to_delete.lower() == "y":
            Snack_List.remove(snack)
            save_data()
            print("Snack Deleted Successfully!")
            start();
        else:
            start()

# Function to add a new snack
def Add_Snack():
    load_data()

    try:
        id = len(Snack_List) + 1
        snack_name = input("Enter the snack name: ")
        snack_price = input("Enter the snack price: ")
        snack_quantity = int(input("Enter the snack Quantity available: "))
        snack_details = {
            "id": id,
            "name": snack_name,
            "price": snack_price,
            "Quantity": snack_quantity
        }
        Snack_List.append(snack_details)
        save_data()
        print("Snack added successfully!!")
        start()
    except ValueError:
        print("Please enter a valid input")
        Add_Snack()

# Function to display the list of snacks
def ShowSnack():
    load_data()
    print("Here is the snack List! \n")
    for i in range(0, len(Snack_List)):
        print("================================================================\n")
        print("Snack:", Snack_List[i]["name"])
        print("Snack price:", Snack_List[i]["price"])
        print("Snack Quantity:", Snack_List[i]["Quantity"])
        print("================================================================\n")

    start()

# Function to update a snack
def updateSnack():
    id_of_snack = int(input("Enter the Snack Id you want to update: "))
    snack = None
    for i in Snack_List:
        if i["id"] == id_of_snack:
            snack = i
            break

    if snack is None:
        print("Snack not found. Please enter a valid Snack ID.")
        updateSnack()
    else:
        print("Found Snack:")
        print("Snack ID:", snack["id"])
        print("1) Snack:", snack["name"])
        print("2) Snack price:", snack["price"])
        print("3) Snack Quantity:", snack["Quantity"])

        try:
            choosedOption = int(
                input("What you want to update from the above options: "))
            if choosedOption == 1:
                new_Name_for_snack = input(
                    "Enter the updated name for the snack: ")
                snack["name"] = new_Name_for_snack
                save_data()
                print("Snack name updated Successfully!!")
            elif choosedOption == 2:
                new_Name_for_price = input(
                    "Enter the updated price for the snack: ")
                snack["price"] = new_Name_for_price
                save_data()
                print("Snack price updated Successfully!!")
            elif choosedOption == 3:
                new_Name_for_Quantity = input(
                    "Enter the updated Quantity for the snack: ")
                snack["Quantity"] = new_Name_for_Quantity
                save_data()
                print("Snack Quantity updated Successfully!!")
            start()
        except ValueError:
            print("Please Enter a valid Input!!")

# Call the greet function to start the program
greet()
