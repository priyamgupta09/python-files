#program without DP
'''def checkUgly(num):
    while(num%2 == 0):
        num /= 2
    while(num%3 == 0):
        num /= 3
    while(num%5 == 0):
        num /=5
    if(num==1):
        return True
    else:
        return False

def uglyNum(num):
    i,count=2,0
    if(num==1):
        return 1
    while(count!=num-1):
        if(checkUgly(i)):
            count+=1
        i+=1
    return i-1

print(uglyNum(150))'''

#program with DP

def UglyNum(num):
    i=1
    numList = [1]*num
    x,y,z = 0,0,0
    nextUglyNum2=numList[x]*2
    nextUglyNum3=numList[y]*3
    nextUglyNum5=numList[z]*5

    while(i<num):
        nextMin = min(nextUglyNum2,nextUglyNum3,nextUglyNum5)
        numList[i] = nextMin

        if(numList[i]==nextUglyNum2):
            x+=1
            nextUglyNum2=numList[x]*2
        if(numList[i]==nextUglyNum3):
            y+=1
            nextUglyNum3=numList[y]*3
        if(numList[i]==nextUglyNum5):
            z+=1
            nextUglyNum5=numList[z]*5
        i+=1
    return numList

print(UglyNum(150))
        