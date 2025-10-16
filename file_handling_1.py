with open("codengal.txt", 'w') as f: 
    f.write("I love doing coding. It is very much fun.") 
f.close()   

with open("codengal.txt", 'w') as f: 

    data = f.readlines() 

    for line in data:
        word = line.split() 
        print(word) 

f.close()