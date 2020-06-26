package fractional_knapsack_problem;

import java.util.Scanner;
public class Fractional_knapsack_problem {

    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc=new Scanner(System.in);        
        float p[]=new float[3];
        float w[]=new float[3];
        float pw[]=new float[3];
        float max=20,tp=0,tw=0,rw=0;
        int last=0,no_object=0;
        
        System.out.println("Enter weight and profit for objects");
        for(int i=0;i<3;i++)
        {
            System.out.println("Enter Weight for object"+(i+1));
            w[i]=sc.nextInt();
            
            System.out.println("Enter profit for object"+(i+1));
            p[i]=sc.nextInt();
            
            pw[i]=(p[i]/w[i]);
        }        
        System.out.println("Your input...");
        System.out.println("Weight\tProfit");
        System.out.println("-------------------------");
        
        for(int i=0;i<3;i++)
        { 
           System.out.println(w[i]+"\t"+p[i]);
           System.out.println("-------------------------");        
        }        
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<2;j++)
            {
                if(pw[j]<pw[j+1])
                {
                    float temp1=pw[j];
                    pw[j]=pw[j+1];
                    pw[j+1]=temp1;
                    
                    float temp2=w[j];
                    w[j]=w[j+1];
                    w[j+1]=temp2;
                    
                    float temp3=p[j];
                    p[j]=p[j+1];
                    p[j+1]=temp3;
                }
            }                        
        }
                              
        for(int k=0;k<3;k++)
        {
            if(w[k]<=max)
            {
                max= max-w[k];
                tp=tp+p[k];
                last=k;
                no_object++;
            }                       
        }
        
        if(max>0)
        {
        tp=tp+(max/w[(last+1)])*p[(last+1)];
        no_object++;
        }
        System.out.println("total profit:"+tp);
        System.out.println("Total object used:"+no_object);
    }
    
}
