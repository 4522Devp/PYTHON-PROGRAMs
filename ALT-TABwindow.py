
'''
arr[]= {3,5,2,4,1} k = 3
4,3,5,2,1

arr[0]= current app
arr[1] = most recent
arr[n-1] = least recent used

if i click tab button three time 3rd element will be the first element in the array
'''

def altTab(a,n,k):
    index = 0
    index = k%n # 3%5 = 3
    x = index
    id = a[index]

    while x > 0:
        p = x
        x-=x # 2
        a[p]= a[x]
    
    a[0]=id

a = [3,5,2,4,1]
n = len(a)
k = 4

altTab(a,n,k)
for i in range(0,n):
    print(a[i]," ")