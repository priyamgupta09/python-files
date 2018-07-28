#Factorial using tabulation DP

def fact(x):
    f=[0]*100

    f[0]=1
    for i in range(1,x+1):
        f[i] = f[i-1] * i
    
    return f[x]

#print(fact(0))

#Factorial using Memoization DP

def fac(arr, x):
    if(x==0):
        arr[x]=0
        return 1
    
    if(arr[x]!=-1):
        return arr[x]

    arr[x] = x * fac(arr,x-1)
    return arr[x]

#arr = [-1]*7
#print(fac(arr, 6))
#print(arr[:7])

#fibonacci recursive

"""def fibo(x):
    if(x==0 or x==1):
        return x

    return fibo(x-1) + fibo(x-2)

print(fibo(6))"""

#fibonacci recursive using DP memoization 

'''def fibo(arr, x):

    if(x==0 or x==1):
        arr[x] = x
        return x

    if(arr[x]!=-1):
        return arr[x]

    arr[x] = fibo(arr, x-1) + fibo(arr, x-2)
    return arr[x]

arr = [-1]*15
print(fibo(arr, 6))
print(arr)'''

#fibonacci recursive using DP tabulation

def fibo(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2,n+1):
        f[i]=f[i-1] + f[i-2]
    
    return f[n]

print(fibo(6))


