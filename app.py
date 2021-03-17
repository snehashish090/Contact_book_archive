# Made by Snehashish Laskar
# Made on 17-03-2021
# Developer contact: https://github.com/snehashish090 or snehashish.laskar@gmail.com
import json 

def list_of_commands():
    print("type a to add a new contact")
    print("type l to look for a contact ")
    print("type rm to remove a contact")
    print("type q to quit")

with open("data.json", "r") as file:
    data = json.load(file)

def Add_Contact():
    name = input("enter the name of this person: ")
    email  = input("enter the email address of this person: ")
    number = input("enter the phone number: ")
    with open ("data.json", "w") as file:
        data.append({'name': name, 'email': email, "phone": number})
        json.dump(data, file)
    print(f"added contact with name {name} ")

def Lookup_Contact():
    name  = input("enter the name/email/phone no. of the person you want to look up: ")
    for i in data:
        if i["name"] == name or name == i["phone"] or i["email"] == name: 
            print(i)
        else:
            print("contact does not exist")

def Remove_Contact():
    with open ("data.json", "w") as f:
        name  = input("Enter the name of the person you want to remove: ")
        for i,j in enumerate(data):
            if j["name"] == name:
                del data[i]
                print("deletd contact!")
        json.dump(data, f)


commands  = {"rm" : Remove_Contact, "a" : Add_Contact, "l" : Lookup_Contact, "q" : exit, "s" : list_of_commands}    

while True:
    command = input(">")
    for i,y in commands.items():
        if i == command:
            y()

    
