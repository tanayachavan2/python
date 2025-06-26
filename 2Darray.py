import numpy as np 
grades=np.array([[87,96,70], [100,30,50],[77,55,66], [23,57,80]])

print(grades[0,1]) #row0 column1
print(grades[1,3])
print(grades[0:2])#prints 0 and 1 row excluding 2nd row 
print(grades[1])#prints 1st row

#subset selection of 2D array's columns
print(grades[0,2])
print(grades[:, 1:3])#shows columns
print(grades[:, 0])#shows columns


#reshape and resize and transposing
grade_s=np.array([[87,96,70], [100,30,50]])
print(grade_s.reshape(1,6))
print(grade_s)

print(grade_s.resize(1,6))#resize modifies original array's shape

flattened=grade_s.flatten()
print(flattened)
print(grade_s)

raveled=grade_s.ravel()
print(raveled)
print(grade_s)

raveled[0]=100
print(raveled)
print(grade_s)

print(grade_s.T)#transposing rows and columns

grades2=np.array([[22,33,44], [22,55,77]])
np.hstack((grade_s, grades2))
np.vstack((grade_s, grades2))

