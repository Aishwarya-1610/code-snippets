int equalPartition(int n, int arr[]){
        int sum = 0; 
        for(int i = 0; i<n; i++) sum += arr[i];
        if(sum&1) return 0;
        sum /= 2;
        int dp[n+1][sum+1] = {};
        for(int i = 0; i<n+1; i++) dp[i][0] = 1;
        for(int i = 1; i<n+1; i++){
            for(int j = 1; j<= sum; j++)
                if(dp[i-1][j] || (arr[i-1] <= j && dp[i-1][j-arr[i-1]])) 
                    dp[i][j] = 1;
        }
        return dp[n][sum];
    }
