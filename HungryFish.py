from datetime import datetime

def CalMinMoves(key, fishes):
    fishes.sort()
    moves=0
    n=len(fishes)
    for i in range(len(fishes)):
        if(moves==n):
            break
        c=0
        while fishes[i] >= key and c<len(fishes[i:]):
            key=key*2-1
            c+=1
        else:
            if(fishes[i]>=key):
                moves+=c
                return moves
            moves+=c
            key+=fishes[i]
    return moves
        

startTime=datetime.now()
s="10#50,60,70,80,1000,2000,3000"
x,y=s.split('#')
x=int(x)
y=[int(i) for i in y.split(',')]
print(CalMinMoves(x,y))
print('Total Time',datetime.now()-startTime)