    int getMiddle(Node *head)
    {   
         int l =0;
        struct Node *p = head;
        while(p!=NULL){
            l++;
            p= p->next;
            
        }
          p = head;
          int ans = l/2;
          while(ans>0){
              p = p->next;
              ans--;
              
          }
          return(p->data);
