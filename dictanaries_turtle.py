def no_notes(a): 

    Q = [2000, 500, 200, 100, 50, 20, 10,] 
    x = 0 

    for i in range(7): 

        q = Q[i] 
        x = a // q 
        print("notes of [] = {}". format(q,x)) 

        a = a % q 

amount = int(input("enter the amount here")) 

no_notes(amount) 

my_tuple = {} 
print(my_tuple) 

my_tuple = (1, 2, 3, 4, 5,) 
print(my_tuple) 

my_tuple = (1, "hello", [1, 2, 3, "hi"]) 
print(my_tuple) 

my_tuple = (1, 2, 3, (4, 5, 6,), ["hi", "hello" 4])
print(my_tuple) 

my_tuple = ("w", "e", "r", "y", "s", "f", "g") 
print(my_tuple[4]) 
print(my_tuple[2]) 

n_tuple = (1, 2, 3, (4, 5, 6,), ["hi", "hello" 4]) 

print(n_tuple[3][1])
