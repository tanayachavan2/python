import pandas as pd
grades_dict={
    'Wally':[87,88,89], 'Eva':[100,102,103],
    'Sam':[99,97,94], 'Kat':[100,82,85],
    'Tanaya':[88,99,77]
}

grades=pd.DataFrame(grades_dict)
print(grades)
grades.index=['Test1', 'Test2', 'Test3']
print(grades)

#selecting subsets of rows and columns
subset=grades.loc['Test1':'Test2',['Eva','Tanaya']]
print(subset)
subset=grades.iloc[[0, 2], 0:3]#(0,2)represents zeroth index and second index and 0:3 depicts column numbers from 0 to 3
print(subset)

#boolean indexing
gd=grades[grades>=90]
print(gd)
gd=grades[(grades>=80) & (grades<90)]
print(gd)

#aaccessing dataframe cell by row and column
row=grades.at['Test1','Eva']
print(row)
row=grades.iat[2,0]
print(row)

gd=grades.at['Test2','Eva']=100
print(gd)

gd=grades.iat[1,2]=80
print(gd)

descriptive=grades.describe()
print(descriptive)

#pd.set_option('precision', 2)
#des=grades.describe()
#print(des)

total=grades.mean()
print(total)

transpose=grades.T
print(transpose)

transpose=grades.T.describe()
print(transpose)

mean_1=grades.T.mean()
print(mean_1)