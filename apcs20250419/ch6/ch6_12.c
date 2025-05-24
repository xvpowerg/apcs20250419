/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{  
   int i,k;
   for (i = 2; i<= 9; i++){
       for(k= 1; k <= 9; k++){
           printf("%d*%d=%2d ",i,k,i*k);
       }
       printf("\n");
   }
    return 0;
}