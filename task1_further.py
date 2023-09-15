banquet_guests = ["Bastien", "Nicolas", "William", "Max"]

def check_guest(name):
    if name in banquet_guests:
        print("Welcome in!")
    else:
        print("Get lost!")

# Input the name to check
name_to_check = input("Enter a name: ")

# Call the function to check the name
check_guest(name_to_check)
