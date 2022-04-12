vector<int> v;
    
    void inorder(Node* root)
    {
        if (root==NULL)
            return;
       	inorder(root->left);
       	v.push_back(root->data);
       	inorder(root->right);
    }
    
    int kthLargest(Node *root, int k)
    {
        inorder(root);
        int n = v.size();
        return v[n-k];
    }
