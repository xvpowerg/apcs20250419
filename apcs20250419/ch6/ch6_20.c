/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{  float myNumber[5] = {1.2,3.4,5.7,8.3,6.5};
    printf("%.2f\n",myNumber[0]);
    int i = 3;
    printf("%.2f\n",myNumber[i]);
    printf("%.2f\n",myNumber[2]);
    myNumber[2] = 9.5;
    printf("%.2f",myNumber[2]);
    return 0;
}