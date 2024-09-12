#use of title ,strip, lower, upper.
#to use these methods we need to use dot notation like with format.

user_name="hii i am tanaya"
upper1 =user_name.upper()           #upper turn the entire string to uppercase.
title1=user_name.title()            #title turns the enitre string to title case i.e every word starts with the capital letter and other turns to lowercase.
strip1=user_name.strip()            #strip gives shiny new string and removes extra space from both the ends.
capitalize1=user_name.capitalize()  #capitalize it turns the first character to uppercase with rest being lowercase

print(f"{upper1}")
print(f"{title1}")
print(f"{strip1}")
print(f"{capitalize1}")
