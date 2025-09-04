lst = ["Apple", "Banana", "Cherry", "Mango", "Kiwi"] 

print("length of the list", len(lst)) 

print("first element of list", lst[0])

print("last element of list", lst[-1])

lst.append('Papaya') 
print("updated list", lst) 

lst.remove("Banana") 
print("updated list", lst) 

lst.sort() 
print("updated list", lst) 

lst.pop("2")
print("updated list", lst)

lst.reverse() 
print("reversed list", lst) 

print("Multiplication of list", 2 * lst) 

lst[:4] 
print("sliced list", lst) 

lst.clear() 
print("Cleared list", lst) 