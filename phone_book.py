import sys  

def initial_phonebook():
    
    row,cols = int(input("please enter the enitial number of the contacts")), s 

phonebook = [] 
print(phonebook) 

for i in range(row):
    
    tem = [] 

    for j in range(cols): 
         
            if j == 0: 
             tem.append(str(input("enter a name :*"))) 

            if tem [j] == "" or temp[j] == " " : 
                 sys.exit 

            if j == 1: 
             tem.append(int(input("enter a number :*")))  

            if j == 2: 
             tem.append(str(input("enter a email adderess :*"))) 

            if tem [j] == "" or temp[j] == " " : 
                 temp[j] = None 

            if j == 3: 
             tem.append(str(input("enter a dd/mm/yy :*"))) 

            if tem [j] == "" or temp[j] == " " : 
                 temp[j] = None  

            if j == 4: 
                tem.append(str(input("enter category family/frinds/work others :*"))) 

            if tem [j] == "" or temp[j] == " " : 
                 temp[j] = None  

        phonebook.apppend(temp) 
    print(phonebook)
    return phonebook

 
def menu(): 
    print("***********************") 
    print("smart phone directory **********")
    print("******************************************")  
    print("1. add a new contact") 
    print("2. Remove an existing contact ") 
    print("3. Delete all contact") 
    print("4. Search for a contact") 
    print("5. display all contacts") 
    print("6. exit phonebook") 

    choice(input("enter a choice")) 

    return choice 
     

def add_contact(pb): 

    dip = [] 

    for i in range(len(pb[0])): 

        if i == 0: 
            dip.append(str(input("enter a name :*")))
        if i == 1: 
            dip.append(int(input("enter a number here :*")))
        if i == 2: 
            dip.append(int(input("enter a email adderess here :*")))
        if i == 3: 
            dip.append(int(input("enter a dd/mm/yy here :*")))
        if i == 4: 
            dip.append(int(input("enter a category family/friends/ work others here :*"))) 

    pb.append(dip) 
    return(pb) 

def remove_exsisting(pb): 

    query = input("enter the name you want to remove: ") 
    temp = 0 

    for i in range(len(pb)): 

        if query == pb[i][0] 
        temp += i  



    if temp = 0: 
            print("sorry , you have entered a wrong name") 

    return pb

def dellet_all(pb): 
     
     return pb.clear() 
 
 def search existing(pb): 
     choice = int(input(enter search catagory))=





            




             

            
             


             









































def display_all(pb): 
     
     if not pb:
         ptint("the list is empty") 
    else: 

         for i in range()

         



































