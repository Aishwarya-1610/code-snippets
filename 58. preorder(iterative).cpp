vector<int> preOrder(Node* root)
    {
        vector<int> ans;
        stack<Node*> st;
        Node* curr= root;
        while(curr!=NULL || st.empty()== false){
            
            
            while(curr!=NULL){
                st.push(curr);
                ans.push_back(curr->data);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            curr = curr->right;
        }
        return ans;
