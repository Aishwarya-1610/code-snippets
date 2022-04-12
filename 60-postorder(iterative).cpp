vector<int> postOrder(Node* node) {
        vector<int> ans;
        stack<Node*> s;
        s.push(node);
        while(!s.empty()){
            Node* temp = s.top();
            ans.push_back(temp->data);
            s.pop();
            if(temp->left!=NULL){
                s.push(temp->left);
            }
            if(temp->right!=NULL){
                s.push(temp->right);
            }
            
        }
        reverse(ans.begin(),ans.end());
        return ans;
