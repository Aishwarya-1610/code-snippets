bool isValidBST(Node *root, int min, int max)
    {
        if(!root) return true;
        if(root->data <= min || root->data >= max) return false;
        return (isValidBST(root->left, min, root->data) && isValidBST(root->right, root->data, max));
    }
    bool isBST(Node* root) 
    {
        // Your code here
        return isValidBST(root, INT_MIN, INT_MAX);
    }
