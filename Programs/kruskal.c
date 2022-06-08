#include<stdio.h>
typedef struct edge{
    int source,destination,weight;
}edge;

void sort_weight(edge input[],int n,int E){
    edge temp;

    for (int i=0;i<(E-1);i++){
        for (int j=0;j<(E-i-1);j++){
            if(input[j].weight > input[j+1].weight){
                temp=input[j];
                input[j]=input[j+1];
                input[j+1]=temp;
            }
        }
    }
}

int find_parent(int v,int parent[]){
    if(parent[v]==v){
        return v;
    }
    return find_parent(parent[v],parent);
}

void kruskals(edge input[],int n,int E){

    //sorting the edges in ascending order
    sort_weight(input,n,E);
    //creating the output array of size E-1

    edge output[E-1];

    int parent[n];
    for(int i=0;i<n;i++){
        parent[i]=i;
    }

    int count=0; //counter for the number of edges in the output array
    int i=0; //counter for checking all the edges 
    while(count<n-1){
        edge current=input[i];

        int s_parent=find_parent(current.source,parent);
        int d_parent=find_parent(current.destination,parent);

        if(s_parent!=d_parent){
            output[count]=current;
            count++;

            parent[s_parent]=d_parent;
        }
        i++;
    }
    printf("The edes included in MST are:\n");
    for (int i=0;i<count;i++){
        printf("%d -> %d ,weight= %d\n",output[i].source,output[i].destination,output[i].weight);
    }
}

int main(){
    int n,E;
    printf("Enter the number of vertices:");
    scanf("%d",&n);
    printf("Enter the number of Edges:");
    scanf("%d",&E);
    edge input[E]; // input array of type edge
    for(int i=0;i<E;i++){
        int s,d,w;
        printf("Enter edge in format source destination weight ");
        scanf("%d %d %d",&s,&d,&w);
        input[i].source=s;
        input[i].destination=d;
        input[i].weight=w;
    }
    
    kruskals(input,n,E);
    
    return 0;
}