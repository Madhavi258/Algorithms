#include<stdio.h>
#include<stdlib.h>
int main()
{
int n=100;
int a[n],data,key,flag=1;
time_t t1,t2,total;

for(int i=0;i<100;i++)
{
    a[i]=i;
}
printf("enter element which you want to search:");
scanf("%d",&key);
t1 = time(NULL);
for(int j=0;j<100;j++)
{
if(a[j]==key)
{
printf("\nvalue is found at position:%d",j);
flag=0;
}

}
if(flag==1)
printf("\nelement is not found");

t2 = time(NULL);
total=t2-t1;
printf("\nTotal time: %ld\n", total);
return 0;
}
