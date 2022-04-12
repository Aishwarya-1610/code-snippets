int rowWithMax1s(vector<vector<int> > arr, int n, int m) {
    // code here
    int a=-1,b=0;
    for(int i=0;i<n;i++){
        int s=0;
        for(int j=0;j<m;j++) if(arr[i][j]) s++;
        if(s>b){
            b=s;
            a=i;
        }
    }
    return a;
}
