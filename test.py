def replaceElements(arr): 
        
        if len(arr) == 1:
            return -1
       
        arr[-1] = -1

        for i in range(len(arr)-2, -1,-1):

            temp = max(arr[i],arr[i-1])
            arr[i] = temp
            
            
        print(arr)

replaceElements([17,18,5,4,6,1])