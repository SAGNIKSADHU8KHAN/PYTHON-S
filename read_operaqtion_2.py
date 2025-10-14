file = open("codingal.txt" 'r') 
print("Open only the first line") 
print(file,readline()) 

file.closed() 

file = open("codingal.txt" 'r') 
print("read mutiple  line")  
print(file,readline()) 

file.closed() 

file = open("codingal.txt" 'r') 

print("loop through the lines")

for line in file: 
    print(file) 
file.closed