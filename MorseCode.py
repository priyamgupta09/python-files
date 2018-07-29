from datetime import datetime

morseCodesList=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--',
            '-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
count=0

def MorseCode(word):
    codeList=list(word.upper())
    codeList=[ord(x)-65 for x in codeList]
    morseCode = [morseCodesList[x] for x in codeList]
    return ''.join(morseCode)

def PossibleWords(code, n):
    global morseCodesList
    global count
    if(n==1):
        for i in range(len(morseCodesList)):
            if(code==morseCodesList[i]):
                count+=1
                return 1
        else:
            return 0

    for i in range(len(morseCodesList)):
        if(code.startswith(morseCodesList[i]) and len(code)>len(morseCodesList[i])):
            PossibleWords(code[len(morseCodesList[i]):],n-1)

startTime = datetime.now()
code = MorseCode('PriyamGupt')
PossibleWords(code, 10)
print(count)
print('Total Time=',datetime.now() - startTime)
