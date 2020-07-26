#include <stdio.h>
#include <stdlib.h>
#define INF 9999
void DFS(int v);
int visited[20],adj[20][20],path[20];
int n=0,pos=0,source,goal;
void main()
{

    printf("Enter No. Vertices in Graph:");
    scanf("%d",&n);
    printf("[Notice: Remember vertices started from 0]");
    printf("f\nEnter Source Vertex:");
    scanf("%d",&source);
    printf("Enter Goal Vertex:");
    scanf("%d",&goal);
    for(int i=0;i<n;i++)
    {
        visited[i]=0;
        path[i]=INF;
        for(int j=0;j<n;j++)
        {
            adj[i][j]=0;
        }
    }

    printf("\nEnter 1 if given vertices are connected otherwise enter 0...\n");
    for(int i=0;i<n; i++)
    {
        for(int j=0;j<n; j++)
        {
            if(i!=j)
            {
                printf("Vertex %d & Vertex %d:",i,j);
                scanf("%d",&adj[i][j]);
                //adj[j][i]=adj[i][j];

            }
        }
    }
    for(int i=0;i<n; i++)
    {
        for(int j=0; j<n;j++)
        {
            printf("%d  ",adj[i][j]);
        }
        printf("\n");
    }
    DFS(source);
}

void DFS(int v)
{
    visited[v]=1;
    path[pos]=v;
    pos++;
    for(int i=0;i<n;i++)
    {
        if(adj[v][i]==1)
        {
            if(visited[i]==0)
            {
                DFS(i);
            }
        }
    }
    if(v==goal)
    {
        printf("\nPATH:\n");
        for(int i=0;i<n;i++)
        {
            if(path[i]!=INF)
            {
                printf("%d ",path[i]);
            }
            if(path[i]==goal)
            {
                break;
            }
        }
    }
}
