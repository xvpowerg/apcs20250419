/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
int getFibo(int n){
    if (n==0){
        return 0;
    }else if(n == 1){
        return 1;
    }else{
        return getFibo(n-1) + getFibo(n-2);
    }
    
}

int main()
{  printf("f(6):%d",getFibo(6)); 
    return 0;
}