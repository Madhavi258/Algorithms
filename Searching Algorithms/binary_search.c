#include<stdio.h>
#include<stdlib.h>
int main()
{
int a[1000],key,low=0,high=999,mid,flag=1;
time_t t1,t2,total;
for(int i=0;i<1000;i++)
{
    a[i]=i;
}
printf("enter value that you want to search:");
scanf("%d",&key);
t1 = time(NULL);
while(low<=high)
{
mid=(low+high)/2;
if(key==a[mid])
{
printf("your value is found at position:%d",a[mid]);
flag=0;
break;
}
else if(key<a[mid])
{
high=mid-1;
}
else
{
low=mid+1;
}
}
if(flag==1)
{
printf("element is not found");
}
t2 = time(NULL);
total=t2-t1;
printf("\nTotal time: %ld\n", total);
return 0;
}
