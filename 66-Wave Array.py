def convertToWave(self,arr,N):
        i =0
        while i<N-1:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            i +=2
            
        return arr 
