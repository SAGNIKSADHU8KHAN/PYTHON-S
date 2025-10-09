file = open("codingal.txt") 

content = file.read() 
count = 0 

line = content.split("\n") 

for i in line: 

    if i: 
         count += 1 

print("the line of the file is", count)

    
    
