class Palindrome:
    def checkPalindrome(self, num):
        if(num==num[::-1]):
            return True
        else:
            return False
    
    def nextPalindrome(self, num, n):
        if(n==2):
            if(num==10):
                num+=1
            elif(num!=99):
                num+=11
            else:
                num+=2
        elif(list(str(num)).count('9')==n):
            num+=2
        elif(n%2==0):
            mid=n//2
            if((str(num)[mid-1:mid+1])!="99"):
                num+=(11*(10**(mid-1)))
            else:
                while(str(num)[mid]=='9'):
                    mid+=1
                num+=(11*(10**(n-mid-1)))
                
        else:
            mid=n//2
            if((str(num)[mid])!='9'):
                num+=((10**(mid)))
            else:
                while(str(num)[mid]=='9'):
                    mid+=1
                num+=(11*(10**(n-mid-1)))
        return num

obj = Palindrome()
a=input()
n=len(a)
print(obj.nextPalindrome(int(a),n))



