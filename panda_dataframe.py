import pandas as pd

grades=pd.Series([30,40,50])
print(grades)

gd=pd.Series(98,range(3))
print(gd)

print(grades[0])

print(grades.count())
print(grades.mean())
print(grades.max())
print(grades.min())
print(grades.std())
print(grades.describe())

#creating series with custom indices
grades=pd.Series([30,40,50], index=['Tanaya','Shivani','Madhura'])
print(grades)

#dictionary initializer
grades=pd.Series({'Tanaya':50, 'Shivani':44, 'Madhura':90})
print(grades)

"""accesing elements"""
print(grades['Tanaya'])
print(grades.Shivani)
print(grades.values)
print(grades.dtype)

names=pd.Series(['Tanaya','Shivani','Madhura'])
print(names.str.contains('a'))
print(names.str.upper())