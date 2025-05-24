/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   
    int number1;
    float input2;
    char input3[10];
    printf("輸入整數:");
    scanf("%d",&number1);
    printf("number1:%d \n",number1);
    
    printf("請輸入浮點數:");
    scanf("%f",&input2);
    printf("input2:%f \n",input2);
    
    printf("輸入文字:");
    scanf("%10s",&input3);
    printf("文字:%s\n",input3);
    
    return 0;
}