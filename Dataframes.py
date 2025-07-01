import pandas as pd

#DataFrame is 2Darray
grades_dict={
    'Wally':[87,88,89], 'Eva':[100,102,103],
    'Sam':[99,97,94], 'Kat':[100,82,85],
    'Tanaya':[88,99,77]
}

grades=pd.DataFrame(grades_dict)
print(grades)

grades.index=['Test1', 'Test2', 'Test3']
print(grades)

EV=grades['Eva']
print(EV)

tan=grades.Tanaya
print(tan)

location=grades.loc['Test1']
print(location)

iloc=grades.iloc[1]
print(iloc)

series=grades.iloc[0:2]
print(series)
series=grades.iloc[[0,2]]
print(series)

random=grades.loc ['Test1':'Test3']
print(random)
random=grades.loc[['Test1','Test3']]
print(random)

