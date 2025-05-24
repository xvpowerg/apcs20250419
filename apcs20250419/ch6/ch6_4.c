/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   
    int v1 = 5;
    int v2 = 2;
    
    printf("%d / %d = %d\n",v1,v2,v1/v2);
    printf("%d / %d = %.2f\n",v1,v2,v1/(float)v2);
    printf("%d %%  %d = %d\n",v1,v2,v1%v2);
    return 0;
}