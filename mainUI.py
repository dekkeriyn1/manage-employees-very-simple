import os
import time
import getpass
import tkinter as tk
from tkinter import messagebox, simpledialog

def display_exit_message():
    for i in range(3, 0, -1):
        print(f"Exiting in {i} seconds...")
        time.sleep(1)

def update_file_path(new_filename):
    global file_path
    file_path = os.path.join(os.getcwd(), f"{new_filename}.txt")
    messagebox.showinfo("File Path Updated", f"File path updated to: {file_path}")

def insert_data():
    n = simpledialog.askinteger("Input", "Enter the number of records:")
    if n is None:
        return
    with open(file_path, "a") as file:
        for _ in range(n):
            emp_id = simpledialog.askstring("Input", "Enter Employee ID:")
            name = simpledialog.askstring("Input", "Enter Name:")
            salary = simpledialog.askfloat("Input", "Enter Salary:")
            department = simpledialog.askstring("Input", "Enter Department:")
            if emp_id and name and salary and department:
                file.write(f"{emp_id},{name},{salary},{department}\n")
    messagebox.showinfo("Success", "Data inserted successfully.")

def delete_data():
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to delete:")
    if emp_id is None:
        return
    with open(file_path, "r") as file:
        lines = [line for line in file if line.strip().split(",")[0] != emp_id]
    with open(file_path, "w") as file:
        file.writelines(lines)
    messagebox.showinfo("Success", "Data deleted successfully.")

def search_data_by_empid():
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to search:")
    if emp_id is None:
        return
    found = False
    with open(file_path, "r") as file:
        for line in file:
            if line.strip().split(",")[0] == emp_id:
                messagebox.showinfo("Employee Found", line.strip())
                found = True
                break
    if not found:
        messagebox.showwarning("Not Found", "Employee not found.")

def search_all_data():
    with open(file_path, "r") as file:
        data = "".join(line.strip() + "\n" for line in file)
    messagebox.showinfo("All Employee Data", data)

def edit_data():
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to edit:")
    if emp_id is None:
        return
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().split(",")[0] == emp_id:
                name = simpledialog.askstring("Input", "Enter New Name:")
                salary = simpledialog.askfloat("Input", "Enter New Salary:")
                department = simpledialog.askstring("Input", "Enter New Department:")
                file.write(f"{emp_id},{name},{salary},{department}\n")
            else:
                file.write(line)
    messagebox.showinfo("Success", "Data edited successfully.")

def change_file_path():
    password = simpledialog.askstring("Password", "Enter your password:", show='*')
    if password == "1234":
        new_filename = simpledialog.askstring("Input", "Change your file path (without .txt extension):")
        if new_filename:
            update_file_path(new_filename)
            with open(file_path, "w") as file:
                messagebox.showinfo("Success", "File path updated and file created successfully.")
    else:
        messagebox.showerror("Invalid Password", "Invalid password. Exiting...")
        display_exit_message()
        root.quit()

def exit_program():
    display_exit_message()
    root.quit()


file_path = os.path.join(os.getcwd(), "employees.txt")


root = tk.Tk()
root.title("Employee Management System")

#
tk.Button(root, text="1. Insert Data", command=insert_data).pack(fill='x')
tk.Button(root, text="2. Delete Data", command=delete_data).pack(fill='x')
tk.Button(root, text="3. Search Data by EmpID", command=search_data_by_empid).pack(fill='x')
tk.Button(root, text="4. Search All Data", command=search_all_data).pack(fill='x')
tk.Button(root, text="5. Edit Data", command=edit_data).pack(fill='x')

tk.Button(root, text="6. Exit", command=exit_program).pack(fill='x')
tk.Button(root, text="Change File Path (Admin Only)", command=change_file_path).pack(fill='x')


root.mainloop()
