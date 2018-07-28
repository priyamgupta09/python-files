def checkUgly(num):
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

print(uglyNum(150))