 int height(Node*root){
       if(root==NULL){
           return 0;
       }
       int l=height(root->left);
       int r=height(root->right);
       return max(l,r)+1;
   }
   int diameter(Node* root) {
       if(root==NULL) return 0;
      int x=diameter(root->left);
      int y=diameter(root->right);
      int h=height(root->left)+height(root->right)+1;
      return max(h, max(x,y));
      
      
   }
