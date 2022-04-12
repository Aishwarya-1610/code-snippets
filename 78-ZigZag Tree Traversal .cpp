 vector <int> zigZagTraversal(Node* root)
    {
    	vector<vector<int>> result;
    	if(root==NULL)
    	return result;
    	queue<Node*>q;
    	q.push(root);
    	bool l_r = false;
    	while(q.empty()==false){
    	    int n= q.size();
    	    vector<int> row(n);
    	    for(int i=0;i<n;i++){
    	        Node* node= q.front();
    	        q.pop();
    	        int index = l_r ? i: (n-i-1);
    	        row[index] = node->data;
    	        if(node->left) 
    	        q.push(node->left);
    	        if(node->right)
    	        q.push(node->right);
    	    }
    	    l_r = !l_r;
    	    result.push_back(row);
    	        
    	    }
    	    return result;
    	    
    	}
    
