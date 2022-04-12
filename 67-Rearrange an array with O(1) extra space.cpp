void arrange(long long arr[], int n) {
        vector<int>v;
        for(int i=0;i<n;i++){
            v.push_back(arr[i]);
        }
        for(int i=0;i<n;i++){
            int temp = v[i];
            arr[i] = v[temp];
        }
        

        
        
    }
