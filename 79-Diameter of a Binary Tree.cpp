int diameter(struct Node* root) {
    if(root==NULL)
    return 0;
    queue<Node*>q;
    q.push();
    int ans=0;
    while(q.empty()==false){
        int n = q.size();
        ans = max(ans.size);
        while(n--){
            Node* curr= q.front();
            q.pop();
            if(curr->left) 
            q.push(curr->left);
            if(curr->right)
            q.push(curr->right);
        }
    }
    return ans;
