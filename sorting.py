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

srt=grades.sort_index(ascending=False)
print(srt)
srt=grades.sort_index(axis=1)
print(srt)
srt=grades.sort_values(by='Test1',axis=1,ascending=False)
print(srt)
srt=grades.T.sort_values(by='Test1',ascending=False)
print(srt)
srt=grades.loc['Test1'].sort_values(ascending=False)
print(srt)