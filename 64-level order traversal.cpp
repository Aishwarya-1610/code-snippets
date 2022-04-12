void printlevel(Node* root){
   if(root==NULL) return;
  queue<Node*> q;
  q.push(root);
  while(q.empty() == false){
    Node* curr= q.front();
    q.pop();
    cout<<curr->data<<" ";
    if(curr->left!=NULL)
      curr = curr->left;
    if(curr->right!=NULL)
      curr = curr->right;
  }
}
    
