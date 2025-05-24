/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{  int score = 0;
   int sum = 0;
   int count = -1;
   while (score != -1){
       count++;
       sum += score;
       printf("請輸入分數-1結束:");
       scanf("%d",&score);
   }
   printf("sum %d \n",sum);
  
   
    return 0;
}