#Regular Expression library
import re

#Function to return the number extracted from a string.
def check(num):
    return re.sub('\D',"",num)
nu=input(prompt)
if nu.startswith('-'):
    print('-'+check(nu))
else:
    print(check(nu))
