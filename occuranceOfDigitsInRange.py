
'''
50 to 60
digit = 5
output = 11'''

def occur(lower,upper,digit):
    count = 0
    for i in range(lower,upper):
        temp = i
        while temp > 0:
            if temp%10 == digit:
                count = count +1
            temp = temp//10
    
    return count

x = 50
y = 60
z =  5

# Function call

print(occur(x,y,z))


