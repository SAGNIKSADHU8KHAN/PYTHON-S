file = open("codingal.txt" 'r') 

print(file.read()) 
file.closed() 

file = open("codingal.txt" 'r') 
print("\n read the parts of the file \n ") 
print(file.raad(s))  

file.closed()

file = open("codingal.txt" 'a') 
file.write("I am a traveller too") 
file.closed()