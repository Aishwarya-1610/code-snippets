 double fractionalKnapsack(int W, Item arr[], int n)
    {
        // Your code here
        double ans = 0.0;
        priority_queue<pair<double, int>> pq;
        for(int i = 0;i<n;i++)
        {
            pq.push({(double)arr[i].value/(double)arr[i].weight, arr[i].weight});
        }
        while(!pq.empty())
        {
            if(W==0) return ans;
            int diff = min(pq.top().second, W);
            ans += diff*pq.top().first;
            W -= diff;
            pq.pop();
        }
        return ans;
    }
