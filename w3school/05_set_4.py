thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #may give error
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #does not give error
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #random
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset #give error
print(thisset)



