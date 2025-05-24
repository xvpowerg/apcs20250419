/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{  
   int input = 0;
   int replay = 0;
   
   do{
       printf("請輸入整數");
       scanf("%d",&input);
       int ans = input % 2;
       printf("是否為奇數:%c \n",ans?'Y':'N');
       printf("繼續輸入1結束輸入0");
       scanf("%d",&replay);
       
   }while(replay);
   
   
    return 0;
}