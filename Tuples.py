#tuples are similar to list written in round brackets().But cannot append or remove the elements u can only add two tupples together.
tuples=("Rolf","Sanjay")
print(tuples)

#set are collection like lists and tuples contains multiple values but dont contain duplicates. Deonated by curly brackets{}.Can add or remove the elements.
people={"Yash"," Ram"," Raj"}
fri=set(people)

user=input("enter your friend name:")

fri.add(user)
print(fri.intersection(people))   #intersection means comparing between two.
print(fri.union())   # union is used to unite sets and give one big set.
