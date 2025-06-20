colors={'red','orange','blue' ,'green'}
print(colors)

print(len(colors))

colo='red' in colors #true
print(colo)
colo='purple' in colors #false
print(colo)
colo='purple' not in colors #true
print(colo)
for color in colors:
    print(color.upper(),end=' ')


#creating set built in function
numbers=list(range(10))+list(range(5))
print(numbers)

print(set(numbers))

#comparison
num= {1,3,5}=={3,5,1}
print(num)

num= {1,3,5}!={3,5,1}
print(num)

num= {1,3,5}<={3,5,1}
print(num)

num= {1,3}<={3,5,1}
print(num)

num= {1,3,5}<{3,5,1}
print(num)

num= {1,3,5}<{7,3,5,1}
print(num)

num= {1,3,5}>={3,5,1}
print(num)
num= {1,3,5}>={3,1}
print(num)
num= {1,3}>={3,5,1}
print(num)
num= {1,3,5}.issubset({3,5,1})
print(num)
num= {1,2}.issubset({3,5,1})
print(num)
num= {1,3,5}.issuperset({3,5,1})
print(num)
num= {1,3,5}.issuperset({3,2})
print(num)
