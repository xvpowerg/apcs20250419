/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{   int ans=0,gus=0;
    srand(time(0));
    ans = (rand() % 5 )+1;
    //printf("%d",ans);
    
    while(1){
        printf("1~5猜一個數字:");
        scanf("%d",&gus);
        if (ans == gus){
            printf("答對了\n");
            break;
        }else{
            printf("答錯了\n");
        }
    }
    return 0;
}