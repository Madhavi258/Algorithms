#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char txt[] = "this is text",pattern[] = "is";
    int n=strlen(txt),m=strlen(pattern);//text length
    for(int i=0;i<=(n-m);i++)
    {
        int j;
        for(j=0;j<m;j++)
        {
            if (txt[i + j] != pattern[j])
            {
                break;
            }
        }
        if(j==m)
        {
            printf("\npattern found at position %d",i);
        }
    }
}
