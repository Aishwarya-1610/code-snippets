void removeLoop(Node* head)
    {
        struct Node *p = head;
        struct Node *q = head;
        while(p!=NULL){
            if(p->data<0){
                q->next= NULL;
                break;
            }
            else {
                p->data = (p->data)*(-1);
                q = p;
                p = p->next;
            
                
            }
        }
