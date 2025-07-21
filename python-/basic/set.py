my_set = {1,2,3,5,22,35,55,13,45,3,8,}
my_set2 = {1,2,3,6,8,5,55,44,4,41,44,8,}
empty_set = set()
print(my_set)
print(empty_set)
my_set.add(411)
my_set.remove(2)
print(my_set)
my_set.discard(3)
print(my_set)
print(4 in my_set)
print(6 in my_set)
print(len(my_set))

my_set.add(147)
print(my_set)

print(my_set|my_set2)
print(my_set.union(my_set2))

x = frozenset([1,4,8])
print(x)

sqr ={my_set**2 for my_set in range(1,6)}
print(sqr)