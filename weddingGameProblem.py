'''
Minimum number of sets with numbers less than Y
input: s ="1234", Y= 30;
output : 3
'''

def WeddingGame(s:str,y:int,l:int):
    count = 0
    num = 0
    flag = 0
    for i in range(0,l):
        num = num *10 +(i-0)# 1
        if (num<=y):
            flag=1
        else:
            if(flag ==1):
                count = count +1
            num = i-0
            flag = 0

            if (num<=y):
                flag = 1
            else:
                num = 0

    if(flag):
        count = count +1
    return count

s = '1234'
l = len(s)
y = 30

print(WeddingGame(s,y,l))

