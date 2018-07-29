#Longest increasing subsequence using memoization

def LIS(arr):

    n=len(arr)
    lis=[0]*n
    lis[-1]=1
    for i in range(n-1,-1,-1):
        max=0
        for j in range(i+1,n):
            
            if(arr[j]>arr[i] and lis[j]>max):
                max=lis[j]
        lis[i]=max+1
    return sorted(lis)[-1]

a=[50,3,10,7,40,80]
print(LIS(a))