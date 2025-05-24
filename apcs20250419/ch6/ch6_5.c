/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   
    int b1 = 0,b2 = 1;
    
    int ans1 = b1 && b2;
    int ans2 = b1 || b2;
    int ans3 = !b2;
    
    printf("%d\n",ans1);
    printf("%d\n",ans2);
    printf("%d\n",ans3);
    
    return 0;
}