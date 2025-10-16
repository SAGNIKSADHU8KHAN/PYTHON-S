new_file = open('newfile.txt', ' x') 
new_file.close() 

import os 

print("Checking if the file does exists or not ...") 

if os.path.exists("codingalupdate.txt"):   
    os.remove("codingalupdate.txt") 
else: 
    print(the file dosent exist) 

    os.rmdir('coding')
