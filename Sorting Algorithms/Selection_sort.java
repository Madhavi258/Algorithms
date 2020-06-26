/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package selection_sort;

/**
 *
 * @author Madhavi
 */
import java.util.Random;
import java.util.Scanner;

class good_input{
    good_input(){
        System.out.println("enter number that you want to enter:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a[]=new int[n];
         //input
         for(int i=0;i<n;i++)
         {
             a[i]=i;
         }
         
         long start_time = System.nanoTime();
         System.out.println("start time for good input:"+start_time);
         
         for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    int temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;
                }
            }
        }
         
         long end_time = System.nanoTime();
         System.out.println("end time for good input:"+end_time);
         
         System.out.println("execution time for good input:"+((end_time-start_time)/1000));
    } 
        
}

class worst_input{
    worst_input(){
        System.out.println("enter number that you want to enter:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a[]=new int[n];
         //input
         for(int i=0;i<n;i++)
         {
             a[i]=n-i;
         }
         
         long start_worst = System.nanoTime();
         System.out.println("start time for worst input:"+start_worst);
         
         for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    int temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;
                }
            }
        }
         
         long end_worst = System.nanoTime();
         System.out.println("end time for worst input:"+end_worst);
         
         System.out.println("execution time for worst input:"+((end_worst-start_worst)/1000));
    } 
    
}

class average_input{
    average_input(){
        System.out.println("enter number that you want to enter:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a[]=new int[n];
         //input
         for(int i=0;i<n;i++)
         {
             Random random=new Random(); 
             a[i]=random.nextInt(1000);
             //System.out.println(a[i]);
         }
         
         long start_average = System.nanoTime();
         System.out.println("start time for average input:"+start_average);
         
         for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    int temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;
                }
            }
        }
         
         long end_average = System.nanoTime();
         System.out.println("end time for average input:"+end_average);
         
         System.out.println("execution time for average input:"+((end_average-start_average)/1000));
    } 
    
    
}


public class Selection_sort {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        good_input obj1=new good_input();
        worst_input obj2=new worst_input();
        average_input obj3=new average_input();
    }
    
}
