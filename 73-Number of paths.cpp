long long  numberOfPaths(int m, int n)
{
    if(m==1 || n==1)
       return(1);
    
    if(m==0 || n==0)
       return(0);
       
    return (numberOfPaths(m,n-1)+numberOfPaths(m-1,n));   
}
