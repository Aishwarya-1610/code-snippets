long long trappingWater(int arr[], int n){
       
       int left[n];
       int right[n];
      long long int sum_water=0;
       
       left[0]=arr[0];
       for(int i=1;i<n;i++)
       {
           left[i]=max(arr[i],left[i-1]);
       }
       
       right[n-1]=arr[n-1];
       for(int i=n-2;i>=0;i--)
       {
           right[i]=max(arr[i],right[i+1]);
       }
       
       for(int i=0;i<n;i++)
       {
           sum_water+=min(left[i],right[i])-arr[i];
       }
       
       return sum_water;
   }
