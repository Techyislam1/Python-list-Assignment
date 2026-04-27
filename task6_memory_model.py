a = [1,2,3]

b = a

b[0]  = 100
print(a)
print(b)
print(id(a))
print(id(b))

#1. because the integer with index 0 is change to 100 and b = a

#2. because they both refer to same thing b = a

#3. it means that if a variable is been assign to another the computer will give them same identity in memory
