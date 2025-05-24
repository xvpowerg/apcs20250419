/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   
    int input = 0;
    int remain = 0;
    printf("請輸入數字:");
    scanf("%d",&input);
    remain = input % 2;
    printf("是否為奇數?:%c\n",remain?'Y':'N');
    
    return 0;
}