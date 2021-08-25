#use any random sets taking by user
E = []
N = []

element_E = int(input("How much element want in set 'E' :"))
for i in range(element_E):
    a = int(input(f'Enter a {i+1} element:\t'))
    E.append(a)
E = set(E)
    
element_N = int(input("How much element want in set 'N' :"))
for j in range(element_N):
    a = int(input(f'Enter a {i+1} element:\t'))
    N.append(a)
N = set(N)
    
print(f'Union of E and N is {E.union(N)}')
print(f'Intersection of E and N is {E.intersection(N)}')
print(f'Difference of E and N is {E.difference(N)}')
print(f'Symmetric Difference of E and N is {E.symmetric_difference(N)}')


#basic code by giving in task 4
'''
E = {2,4,8,0,6}
N = {1,3,5,2,4}

print(N.union(E))
print(N.intersection(E))
print(E.difference(N))
print(E.symmetric_difference(N))
'''
