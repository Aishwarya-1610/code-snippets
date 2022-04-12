struct Node* reverseList(struct Node *head)
    {    struct Node *p =head;
         struct Node *q = NULL;
         struct Node *r = NULL;
         while(p!=NULL){
             r =q;
             q = p;
             p = p->next;
             q->next = r;
         }
            head = q;
        
        
        
        
    }
