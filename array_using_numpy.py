import numpy as np

numbers=np.array([2,3,4,5,6])
print(numbers)

integers=np.array([[2,3,4,5,6], [2,3,4,5,6]])
print(integers)

floats=np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

num=integers.size
print(num)

print(floats.size)

print(integers.itemsize)
print(floats.itemsize)

print(integers.ndim)
print(floats.ndim)

print(integers.shape)
print(floats.shape)

print(np.zeros(5))

print(np.ones((4,6),dtype=int))

print(np.full((2,5),10))

print(np.arange(5))

print(np.arange(5,10))

print(np.arange(10, 1, -1))

#np.arange(1,31).reshape(3,4)


number=np.arange(1,6)
print(number)
print(number*2)
print(number**3)
#numbers += 10


#np.linespace(1.1, 5.5, 5)
numbers2=np.array([8,5,4,2,4,5])



# (numbers[1] *= 10)
# ( numbers[1] /= 10)
# (numbers[2] += 10)

numbers3=numbers[0:3]
print(numbers3)