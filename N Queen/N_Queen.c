#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,mod,even=0,odd=1,oddcount=0,position=0;
    printf("Enter no. of Queens (more than three):");
    scanf("%d",&n);
    int temp=n/2;
    mod=n%12;
    int pos[n],display[n][n];
    for(int i=0;i<n;i++)
    {
        pos[i]=0;
    }

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            display[i][j]=0;
        }
    }

    for(int i=0;i<(n/2);i++)
    {
        even=even+2;
        pos[i]=even;
        position=i;
    }

    if(mod==3 || mod==9)
    {
        for(int i=0;i<(n/2);i++)
        {
            pos[i]=pos[i+1];
        }
        pos[position]=2;
    }
    for(int i=n/2;i<n;i++)
    {
        pos[i]=odd;
        odd=odd+2;
        position=i;
        oddcount=oddcount+1;
    }
    if(mod==8)
    {
        for(int i=0;i<oddcount/2;i++)
        {
            int j=pos[temp];
            pos[temp]=pos[temp+1];
            pos[temp+1]=j;
            temp=temp+2;
        }
    }
    if(mod==2)
    {
        int j=pos[n/2];
        pos[n/2]=pos[(n/2)+1];
        pos[(n/2)+1]=j;

        for(int i=(n/2)+2;i<(n-1);i++)
        {
            pos[i]=pos[i+1];
        }

        pos[n-1]=5;
    }

    if(mod==3 || mod==9)
    {
        for(int i=n/2;i<(n-2);i++)
        {
            pos[i]=pos[i+2];
        }

        pos[n-2]=1;
        pos[n-1]=3;
    }

    for(int i=0;i<n;i++)
    {
        int j=pos[i]-1;
        display[i][j]=1;
    }

    printf("Queens are represented in form of 1s...\n");
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("\t%d",display[j][i]);
        }
        printf("\n\n");
    }

    return 0;
}
