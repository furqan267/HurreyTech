#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv, re
from getpass import getpass

class Employee:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def validateEmail(self):
        email_pattern = "(\w+)@(\w+)\.(\w+)"
        match_object = re.match(email_pattern, self.email)
        if match_object!=None:
            return "Valid email"
        else:
            return "Invalid email"
    def createAccount(self):
        with open('input.csv', 'a', newline="") as f:
            csv_writer_object = csv.writer(f)
            csv_writer_object.writerow([self.email, self.password])
        print("New account created")

        
if __name__ == '__main__':
    while True:
        print("""\n**** WELCOME TO HURREYTECH VENTURES PVT. LTD. ****\n
              1. Login to Hurrey \n
              2. Create New Account \n 
              3. Find Account Password \n
              4. Exit""")
        choice = input("Enter your choice: ")
        if choice=="1":
            email = input("Enter email: ")
            password = getpass("Enter password: ")
            with open('input.csv') as f:
                content = list(csv.reader(f))
                for row in content:
                    if email==row[0] and password==row[1]:
                        print("Welcome to Hurrey")
                        break
                else:
                    print("Sorry user is not registered yet")
        elif choice=="2":
            username = input("Enter username: ")
            passwd = getpass("Entet password: ")
            employee = Employee(username, passwd)
            email_validation = employee.validateEmail()
            if email_validation == "Valid email":
                employee.createAccount()
            else:
                print(email_validation)
                email_validation = employee.validateEmail()
        elif choice=="3":
            user = input("Enter username: ")
            try:
                with open('input.csv') as f:
                    content = list(csv.reader(f))
                    for row in content:
                        if user==row[0]:
                            p = row[1]
                            last_three_letters = p[-3:]
                            revised_password = last_three_letters.rjust(len(p), '*')
                            print("Your password is:", revised_password)
                            break
                    else:
                        print("Sorry user is not registered yet")
            except:
                print("User is not registered yet.")

        elif choice=="4": 
            break
        else:
            print("Please enter valid choice.\n")
    print("Thanks for using. Closing the system.")
else:
    print("Access denied")

