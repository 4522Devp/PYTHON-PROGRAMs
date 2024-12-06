'''
remove outer most paranthesis
input :((()))( () )
output: ()()()


ASCII value of ( -- 40
                ) -- 41
'''

def remove_p(string):
    result =''
    j = 0
    for i in range(0,len(string)):
        if string[i]==41:
            j = j-1
        if (j !=0):
            result = result +string[i]
        if string[i]==40:
            j = j+1

    return result


string = "((()))(())"
print(remove_p(string))
       
