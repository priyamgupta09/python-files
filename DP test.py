p=[2,3,5,1,4]

def profit(year, be, en):
    global p
    if(be > en):
        return 0
    
    a = profit(year+1, be+1, en) + year*p[be]
    b = profit(year+1, be, en-1) + year*p[en]
    return max(a,b)
    
#
#print(profit(1,0,4))
