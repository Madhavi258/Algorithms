#include <stdio.h>
#include <stdlib.h>
void explore(int source);
int pos=0,next=0,flag=0,goal=6;
int visited[11]={0,0,0,0,0,0,0,0,0,0,0};
int q[11]={9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999};
char nodes[11]={'A','B','C','D','E','F','G','H','I','J','K'};
int path[11]={9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999};
int adj[11][11]={
            {0,11,14,7,0,0,0,0,0,0,0},
            {11,0,0,0,15,0,0,0,0,0,0},
            {14,0,0,0,8,10,0,0,0,0,0},
            {7,0,0,0,0,25,0,0,0,0,0},
            {0,15,0,0,0,0,0,9,0,0,0},
            {0,0,10,25,0,0,20,0,0,0,0},
            {0,0,0,0,0,20,0,10,1,0,1},
            {0,0,0,0,9,0,10,0,0,0,0},
            {0,0,0,0,0,0,1,0,0,30,0},
            {0,0,0,0,0,0,0,0,30,0,50},
            {0,0,0,0,0,0,1,0,0,50,0}
            };
int heuristic[7]={40,32,25,35,19,17,0,10};
int front=0,rear=0;
void main()
{
    explore(0);
}
void explore(int v)
{
    visited[v]=1;
    path[pos]=v;
    pos++;
    for(int i=0;i<11;i++)
    {
        if(adj[v][i]>0)
        {
            if(visited[i]==0)
            {
                if(rear == 11)
                {
                    printf("Queue is full");
                }
                else
                {
                    q[rear]=heuristic[i];
                    rear++;
                    visited[i]=1;

                }

            }
        }
    }
    for(int i=0;i<11;i++)
    {
        for(int j=0;j<10;j++)
        {
            if(q[j]>q[j+1])
            {
                int temp=q[j];
                q[j]=q[j+1];
                q[j+1]=temp;
            }
        }
    }
    if(q[0]==9999)
    {
        printf("Failure... No path Found...");
        exit(0);
    }
    else
    {
        int temp=q[front];
        for(int i=0;i<7;i++)
        {
            if(heuristic[i]==temp)
            {
                next=i;
                q[0]=9999;
            }
        }
    }

    if(next != goal)
    {
        explore(next);
    }

    else
    {
        printf("PATH:\n");
        for(int i=0;i<11;i++)
        {
            if(path[i]!=9999)
            {
                int node=path[i];
                printf("%c ",nodes[node]);
            }
        }
        printf("G");
        exit(0);
    }
}
