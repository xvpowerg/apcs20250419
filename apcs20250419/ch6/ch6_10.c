/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   printf("1 Play\n");
    printf("2 Stop\n");
    printf("3 Exit\n");
    int action = 0;
    scanf("%d",&action);
    switch(action){
        case 1:
            printf("Play");
        break;
        case 2:
            printf("Stop");
        break;
        case 3:
            printf("Exit");
        break;
        default:
            printf("Error");
        break;
        
    }
    
    return 0;
}