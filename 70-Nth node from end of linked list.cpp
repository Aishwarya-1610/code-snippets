int getNthFromLast(struct Node *head, int n)
{      struct Node*p = head;
       struct Node*q = NULL;
       struct Node*r = NULL;
       int l =0;
       while(p!=NULL){
           r=q;
           q=p;
           p=p->next;
           q->next =r;
           l++;
       }
       head =q;
       if(l<n){
           return(-1);
       }
       int i=1;
       while(i<n){
           q = q->next;
           i++;
       }
       return(q->data);
    
}
