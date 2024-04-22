import re
db={}
mob=set([])
nameFind={}
def Add(name,number,email):
        db[name]={"Number":number,"Email":email}
        mob.add(number)
        nameFind[number]=name                
def Search(name):
    if name in db:
        print("Name : ",name)
        print("Number :",db[name]["Number"])
        print("Email : ",db[name]["Email"])
    else:
        print("Contact not found.")        
def List():
    if not db:
        print("No contacts saved !!")
    else:
        for n in db:
            Search(n)    
        print("\n")
def Delete(name):
    if name in db:
        number=db[name]["Number"]
        del db[name]
        mob.remove(number)
        del nameFind[number]
        print("Contact was deleted .")
    else:
        print("Contact not found.")
def validPhone(number):
    return number.isdigit() and len(number)==10    
def validEmail(email):
    pattern=r'[\w\._-]+@[A-Za-z]+\.[A-Za-z]+'
    if re.match(pattern,email):
        return True
    else:
        return False        
def continuePrompt():
    response=input("\nDo you want to perform another action ? (yes/no) : ").lower()
    return response=="no"
        
    

def main():
    while True:
        try:
            print("Enter : \n1 for add new contact\n2 for search a contact\n3 for list all contacts\n4 for delete a contact\n5 for exit\n")
            choice=input()            
            if choice=="1":
                name=input("Enter name : ")
                number=input("Enter mobile number : ")      
                if not validPhone(number):
                    print("\nInvalid mobile number!? ,please try again.\n")
                    continue
                email=input("Enter email : ")
                if validEmail(email)==False:
                    print("\nInvalid email id !? ,please try again.\n")
                    continue          
                if number not in mob:
                    Add(name,number,email)
                    print("Contact is saved.")
                else:
                    Option=input("Contact was alredy exit, do you want to replac it ?  (yes/no)\n")
                    option=Option.lower()
                    if option=="yes":
                        Name=nameFind[number]
                        del db[Name]
                        Add(name,number,email)
                        print("Contact is updated.")
                if continuePrompt():
                    print("\nThank you for using contact management system . Exiting....")
                    break                     
            elif choice=="2":
                name=input("Enter name to search contact : ")
                print()
                Search(name)
                if continuePrompt():
                    print("\nThank you for using contact management system . Exiting....")
                    break
            elif choice=="3":
                print()
                List()
                if continuePrompt():
                    print("\nThank you for using contact management system . Exiting....")
                    break
            elif choice=="4":
                name=input("Enter name to delete : ")
                Delete(name)
                if continuePrompt():
                    print("\nThank you for using contact management system . Exiting....")
                    break
            elif choice=="5":
                if continuePrompt():
                    print("\nThank you for using contact management system . Exiting....")
                    break
            else:
                print("Invalid input !!")
            print("\n")            
        except Exception as e:
            print(f"Error : {e}")
if __name__=="__main__":
        main()