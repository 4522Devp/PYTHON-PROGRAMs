'''
bob has to send a code S to his boss. He design a method to encrypt the code using two key values N and M.
The formula that he used to develop the encrypt the code is shown below:
(((S^N%10)^M)%1000000007)

write an algorithm to help bob to encrypt the code
'''

S = int(input("Enter the value of S: "))
M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))

code = S**N
code = code%10
code = code**M
code = code%1000000007

print("The encrypted code is: ",code)
print("THANKYOU")
