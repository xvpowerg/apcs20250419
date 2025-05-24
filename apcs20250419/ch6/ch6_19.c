/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   int number[5] =  {0,1,2,3,4};
    int len = sizeof(number) / sizeof(number[0]);
    printf("len:%d",len);
    return 0;
}