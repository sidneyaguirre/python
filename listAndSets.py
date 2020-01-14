m = int(input())
M= input() 
n = int(input())
N = input()

list_M = M.split() #to get the separate values of the string in the form of a list
list_N = N.split()

newlis_M = list(map(int, list_M)) #to convert all the strings to integers
newlis_N = list(map(int, list_N))

set_M = set(newlis_M) # Creating a set from a list
set_N = set(newlis_N)

dif = set_M.symmetric_difference(set_N) #Returns a set with the symmetric differences of two sets (elements that are not in both sets)

res = list(dif) #transform the set into a list
res.sort() #sort the given list in ascending order

for i in res:
    print(i)