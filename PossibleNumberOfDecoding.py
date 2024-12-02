
'''
input = 123
output = 3

input = 321
output = 2
'''
def decoding(s:str)->int:

    if not s or s[0]=='0':
        return 0
    
    possiblity = [0]*(len(s)+1)
    possiblity[0]=1
    possiblity[1]=1 if s[0] !='0' else 0

    for i in range(2,len(s)+1):
        if s[i-1] != '0':
            possiblity[i]  += possiblity[i-1]

        if s[i-2] == '1'or (s[i-2]=='2' and s[i-1] in '0123456'):
            possiblity[i] +=possiblity[i-2]

    return possiblity[-1]


s = input("enter here: ")
result = decoding(s)
print(result)