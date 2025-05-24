/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   int number[5] = {8,9,18,77,11};
    int len = sizeof(number) / sizeof(number[0]);
    for (int i =0; i< len; i++){
        printf("%d ",number[i]);
    }
    printf("\n");
    return 0;
}