import os
import time
import getpass

def display_exit_message():
    for i in range(3, 0, -1):
        print(f"Exiting in {i} seconds...")
        time.sleep(1)

def update_file_path(new_filename):
    global file_path
    file_path = os.path.join(os.getcwd(), f"{new_filename}.txt")
    print(f"File path updated to: {file_path}")


file_path = os.path.join(os.getcwd(), "employees.txt")

print("Please select choice")
print("1. Insert Data")
print("2. Delete Data")
print("3. Search Data by EmpID")
print("4. Search All Data")
print("5. Edit Data")
print("6. Exit")

choice = int(input("Choose your choice: "))

if choice == 1:
    n = int(input("Enter the number of records: "))
    with open(file_path, "a") as file:
        for _ in range(n):
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            file.write(f"{emp_id},{name},{salary},{department}\n")
    print("Data inserted successfully.")

elif choice == 2:
    emp_id = input("Enter Employee ID to delete: ")
    with open(file_path, "r") as file:
        lines = [line for line in file if line.strip().split(",")[0] != emp_id]
    with open(file_path, "w") as file:
        file.writelines(lines)
    print("Data deleted successfully.")

elif choice == 3:
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(file_path, "r") as file:
        for line in file:
            if line.strip().split(",")[0] == emp_id:
                print(line.strip())
                found = True
                break
    if not found:
        print("Employee not found.")

elif choice == 4:
    with open(file_path, "r") as file:
        print("".join(line.strip() + "\n" for line in file))

elif choice == 5:
    emp_id = input("Enter Employee ID to edit: ")
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().split(",")[0] == emp_id:
                name = input("Enter New Name: ")
                salary = float(input("Enter New Salary: "))
                department = input("Enter New Department: ")
                file.write(f"{emp_id},{name},{salary},{department}\n")
            else:
                file.write(line)
    print("Data edited successfully.")

elif choice == 6:
    display_exit_message()
    exit()

elif choice == 888:
    password = getpass.getpass("Enter your password: ")
    if password == "1234":
        print("Welcome, admin!")
        new_filename = input("Change your file path (without .txt extension): ")
        update_file_path(new_filename)
        with open(file_path, "w") as file:
            print("File path updated and file created successfully.")
    else:
        print("Invalid password. Exiting...")
        display_exit_message()
        exit()

else:
    print("Invalid choice. Please try again.")
