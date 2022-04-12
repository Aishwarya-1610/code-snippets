vector<vector<int>> stockBuySell(vector<int> A, int n){
       int buy=0;
       int sell=-1;
       vector <vector<int>> ans;
       for(int i=1;i<n;i++)
       {
           if(sell==-1 && A[i]<A[buy] )
           {
                buy=i;
           }
          
           else if(sell==-1 && A[i]>A[buy])
           {
               sell=i;
           }
           
           else if(sell!=-1 && A[i]>A[sell])
           {
              sell=i;
           }
           
           else if(sell!=-1 && A[i]<A[sell]) 
           {

               vector <int> v;
               v.push_back(buy);
               v.push_back(sell);
               ans.push_back(v);
               buy=i;
               sell=-1;
               
           }
           
       }
       if(sell!=-1)
       {
           vector <int> v;
           v.push_back(buy);
           v.push_back(sell);
           ans.push_back(v);
       }
       return ans;
       // code here
   }
