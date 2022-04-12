bool detectLoop(Node* head)
    {
        struct Node *p = head;
        struct Node *q = head;
        if((head->next == NULL)||(head == NULL)){
            return false;
        }
        do {
            p= p->next;
            q = q->next;
            q = (q!=NULL)?q->next:q;
            
            
        }while(p && q && p!=q);
        
        
        if(p==q){
            return true;
        }
        else {
            return false;
        }
        
    }
