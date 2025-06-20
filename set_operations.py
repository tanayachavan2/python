#mutable set operations
numbers={1,2,3,4}
numbers |={2,3,5,6}
print(numbers)

numbers.update(range(10))
print(numbers)

numbers.add(20)
print(numbers)

numbers.remove(6)
print(numbers)

numbers.pop()
print(numbers)

numbers.clear()
print(numbers)

#set comprehension
numbers=[1,2,2,3,4,5,6,6,7,8,8,9,10]
evens={item for item in numbers if item %2==0}
print(evens)
