int transitionPoint(int arr[], int n) {
    int c= -1;
    
    for(int i=0; i<=n; i++){
        if((arr[i]==1)&(arr[i-1]==0)){
            return i;
            c++;
            break;
        }
    
        }
       
    if(c<0){
        return(-1);
        
    }    
