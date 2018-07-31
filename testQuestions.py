def highestValuePalindrome(s, n, k):
    #t is min change required
    s=list(s)
    i,j,t=0,n-1,0
    mid=n//2
    mid1=mid if(n%2==0) else mid+1
    while(i<mid and j>=mid1):
        if(s[i]!=s[j]):
            t+=1
        i+=1
        j-=1
    if(k<t):
        return '-1'
    extraMoves = k-t
    if(n==1 and k>=1):
        return '9'
    i,j=0,n-1
    while(i<mid and j>=mid1):
        if(s[i]!=s[j]):
            if(extraMoves>=2 and s[i]!='9' and s[j]!='9'):
                s[i],s[j]='9','9'
                extraMoves-=2
                k-=2
            elif(extraMoves>=1 and (s[i]=='9' or s[j]=='9')):
                s[i],s[j]='9','9'
                extraMoves-=1
                k-=2
            else:
                s[i]=max(s[i],s[j])
                s[j]=s[i]
                k-=1
        elif(s[i]!='9' and extraMoves>=2):
            s[i],s[j]='9','9'
            extraMoves-=2
            k-=2
        i+=1
        j-=1
    if(extraMoves):
        s[mid]='9'
    return ''.join(s)

s='12321'

print(highestValuePalindrome(s,len(s),3))