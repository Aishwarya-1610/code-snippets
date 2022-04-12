int getPairsCount(int arr[], int n, int k) {
       // code here
       int ans=0;
      unordered_map<int,int> m;
      for(int i=0;i<n;i++)
      {
          m[arr[i]]++;
      }
          for(int i=0;i<n;i++)
          {
          ans+=m[k-arr[i]];
          if(k-arr[i]==arr[i])
          {
              ans--;
          }
          
      }
      
      return ans/2;
   }
};
