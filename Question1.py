#Function to convert the reverse of the number

def check(num):
    return str(num)[::-1]
nu=int(input("Enter the number:"))

#The loop checks palindrome. If its not a palindrome
#it adds the reverse to it until it becomes a palindrome.

while True:
    nu=nu+int(check(nu))
    if nu==int(check(nu)):
        break
print(nu)
