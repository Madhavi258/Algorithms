#include <stdio.h>
#include <stdlib.h>
#define inf 9999
int main()
{
    //Finding path from 1 to 6
    int weight[6][6]={
            {0,0,0,0,0,0},
            {0,0,0,0,0,0},
            {0,0,0,0,0,0},
            {0,0,0,0,0,0},
            {0,0,0,0,0,0},
            {0,0,0,0,0,0}
        };
    int distance[6],source[6],adj0[6],adj1[6],adj2[6],adj3[6],adj4[6],adj5[6],dmin=9999,position=0,pflag=0,dis=0,dposition=0,path[6],temp=0;
    int flag[6]={0,0,0,0,0,0};
    static int count0=0,count1=0,count2=0,count3=0,count4=0,count5=0;


        for(int i=0;i<6;i++)
        {
            for(int j=0;j<6;j++)
            {
                if (weight[i][j]==0 && i!=j)
                {
                    printf("Enter Weight from %d to %d:",(i+1),(j+1));
                    scanf("%d",&weight[i][j]);
                    weight[j][i]=weight[i][j];
                }
            }
        }


        //Initialize
        for(int i=0;i<6;i++)
        {
            distance[i]=inf;
            source[i]=0;
        }

        //Source
        distance[0]=0;
        source[0]='\0';


            for(int j=0;j<6;j++)
            {
                //look for adjacent of 0
                if(weight[0][j]!=0)
                {
                    adj0[count0]=j;
                    count0++;
                }

                //look for adjacent of 1
                if(weight[1][j]!=0)
                {
                    adj1[count1]=j;
                    count1++;
                }

                //look for adjacent of 2
                if(weight[2][j]!=0)
                {
                    adj2[count2]=j;
                    count2++;
                }

                //look for adjacent of 3
                if(weight[3][j]!=0)
                {
                    adj3[count3]=j;
                    count3++;
                }

                //look for adjacent of 4
                if(weight[4][j]!=0)
                {
                    adj4[count4]=j;
                    count4++;
                }

                //look for adjacent of 5
                if(weight[5][j]!=0)
                {
                    adj5[count5]=j;
                    count5++;
                }

            }

            while(flag[0]!=1 || flag[1]!=1 || flag[2]!=1 || flag[3]!=1 || flag[4]!=1 || flag[5]!=1)
            {

            //Finding minimum Distance from all non visited vertex
            for(int i=0;i<6;i++)
            {

                if(dmin>distance[i] && flag[i]==0)
                {
                    dmin=distance[i];
                    position=i;
                    pflag=i;
                }
            }
            flag[pflag]=1; //Change flag value for visited vertex
            dmin=9999;

            //Update Distance and Source
            if(position==0)
            {
                for(int i=0;i<count0;i++)
                    {
                        int j=adj0[i];
                        if((distance[j]>distance[0]+weight[0][j]))
                        {
                            distance[j]=distance[0]+weight[0][j];
                            source[j]=0;
                        }
                    }
            }
            else if(position==1)
            {
                for(int i=0;i<count1;i++)
                {
                    int j=adj1[i];
                    if((distance[j]>distance[1]+weight[1][j]))
                        {
                            distance[j]=distance[1]+weight[1][j];
                            source[j]=1;

                        }
                }
            }

            else if(position==2)
            {
                for(int i=0;i<count2;i++)
                {
                    int j=adj2[i];
                    if((distance[j]>distance[2]+weight[2][j]))
                        {
                            distance[j]=distance[2]+weight[2][j];
                            source[j]=2;

                        }
                }
            }

            else if(position==3)
            {
                for(int i=0;i<count3;i++)
                {
                    int j=adj3[i];
                    if((distance[j]>distance[3]+weight[3][j]))
                        {
                            distance[j]=distance[3]+weight[3][j];
                            source[j]=3;

                        }
                }
            }

            else if(position==4)
            {
                for(int i=0;i<count4;i++)
                {
                    int j=adj4[i];
                    if((distance[j]>distance[4]+weight[4][j]))
                        {
                            distance[j]=distance[4]+weight[4][j];
                            source[j]=4;

                        }
                }
            }

            else if(position==5)
            {
                for(int i=0;i<count5;i++)
                {
                    int j=adj5[i];
                    if((distance[j]>distance[5]+weight[5][j]))
                        {
                            distance[j]=distance[5]+weight[5][j];
                            source[j]=5;

                        }
                }
            }

            }

            printf("\n\n1\t|2\t|3\t|4\t|5\t|6\t|\n");
            printf("D S\t|D S\t|D S\t|D S\t|D S\t|D S\t|\n");
            printf("-------------------------------------------------\n");
            for(int i=0;i<6;i++)
            {
                printf("%d ",distance[i]);
                printf("%d\t|",source[i]);

            }

            for(int i=0;i<6;i++)
            {
                if(distance[i]>dis)
                {
                    dis=distance[i];
                    dposition=i;
                }
            }

            printf("\n\nMinimum Distance from 1 to 6: %d\n",dis);
            path[0]=dposition;
            while(dposition!=0)
            {
                for(int i=1;i<6;i++)
                {
                    path[i]=source[dposition];
                    dposition=path[i];
                    temp++;
                }

            }


            printf("Shortest path from 1 to 6: ");
            for(int i=(temp-1);i>=0;i--)
            {
               printf("%d ",path[i]);

            }
        }
