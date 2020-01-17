#include<stdio.h>
void main()
{
    
    float sum,average,x,m;
    printf("enter the values\n");
    for (m = 1; m <=1000; m++)
    {
        scanf("%f",&x);
        sum = sum + x;

    }
    average = sum/(m-1);
    printf("no. of values  = %f\n",m-1);
    printf("sumof the numbers are =%f\n",sum);
    printf("average of the numbers are =%f\n",average);
}
