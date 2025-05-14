#Empty tuple
my_tuple = ()
print (my_tuple)
#Tuple having integers
my_tuple = (1, 2, 3)
print (my_tuple)
#Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print (my_tuple)
#Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print (my_tuple)
#accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])
#nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])
#slicing tuples
print(my_tuple[1:4])
#interating through a tuple
for letter in my_tuple:
    print("hello", letter)

print("-------SET-------")



#sets
my_set = {1, 2, 2, 3, 4, 4} #duplicates not supported
print(set(my_set))
my_set.add(5)
print("Update set",my_set)

set1 = my_set
set2 = {2, 5, 3, 7}

print("\nSet1: ", set1)
print("\nSet2: ", set2)

print("Difference")
print(set1.difference(set2))
print ("Symmetric Difference")
print(set1.symmetric_difference(set2))







