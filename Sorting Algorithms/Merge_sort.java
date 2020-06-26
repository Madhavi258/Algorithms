/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package merge_sort;

/**
 *
 * @author Madhavi
 */
import java.util.Random;

import java.util.Scanner;
class sorting{
    sorting(){
    System.out.println("enter number that you want to enter:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a[]=new int[n];
         //input
        
        System.out.println("Enter 1 for best output\n2 for avarage output\n3 for worst output");
        
        int s=sc.nextInt();
        
        switch(s){   
        case 1:
         for(int i=0;i<n;i++){
            a[i]=i;
         }break;
         
        
        case 2:
            for(int i=0;i<n;i++){
            Random random=new Random(); 
             a[i]=random.nextInt(1000);
            }break;
  
        case 3:
            for(int i=0;i<n;i++){
            a[i]=n-i; 
            }break;
        
        }
         
         long start_time = System.nanoTime();
         //System.out.println("start time for good input:"+start_time);
        mergesort(a,0,(n-1));
        long end_time = System.nanoTime();
         //System.out.println("end time for good input:"+end_time);
         System.out.println("execution time for good input:"+((end_time-start_time)/1000));
         

        
        
         
    }

    void mergesort(int[] a,int p,int r)
        {
            
            
           if(p<r)
            {
                int q=(p+r)/2;
                mergesort(a,p,q);
                mergesort(a,(q+1),r);
                merge(a,p,q,r);
            }
            
        }
    void merge(int[] a,int p,int q,int r)
    {
        int n1=(q-p)+1;
        int n2=r-q;
        
        int left[]=new int[n1];
        int right[]=new int[n2];
        for(int i=0;i<n1;i++)
        {
            left[i]=a[p+i];
        }
        
        for(int j=0;j<n2;j++)
        {
            right[j]=a[q+j+1];
        }
        
       // left[n1+1]=999999;
        //right[n2+1]=999999;

        int i=0;
        int j=0;
        int k=p;
       
    /*for(int k=p;k<r;k++)
    {
        if(left[i]<=right[j])
        {
            a[k] = left[i];
            i++;
        }
        else
        {
            a[k] = right[j];
            j++;
        }
    }*/
        
        while(i < n1 && j < n2)
    {
        if (left[i] <= right[j])
        {
            a[k] = left[i];
            i++;
        }
        else
        {
            a[k] = right[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        a[k] = left[i];
        i++;
        k++;
    }

    
    while (j < n2)
    {
        a[k] = right[j];
        j++;
        k++;
    }

     
    }
    
}
public class Merge_sort {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        sorting obj1=new sorting();
        
    }
    
}
