class MergeSort:
    
    def Merge(self, left, right):
        
        result = []
        i,j = 0,0

        while(len(result) < len(left) + len(right)):
            if(left[i]<right[j]):
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

            if (i==len(left) or j==len(right)):
                result.extend(left[i:] or right[j:])
                break

        return result

    def Divide(self, array):
        n = len(array)
        if(n==1):
            return array
        mid = n//2
        left = array[:mid]
        right = array[mid:n]
        left = self.Divide(left)
        right = self.Divide(right)
        return self.Merge(left, right)
    
arr = [2,4,1,6,8,5,3,7]
obj = MergeSort()
print(obj.Divide(arr))