file1 = open("codingal.txt" 'r') 
file2 = open("codingal_update.txt" 'w') 

for line in file1.readlines(): 

    if not line.starswitch("Codingal"): 

        print(line) 
        file2.write(line) 

file1.closed() 
file2.closed() 