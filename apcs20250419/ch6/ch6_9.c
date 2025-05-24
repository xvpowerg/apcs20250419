/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{   int score = 91;
    if (score >= 90){
        printf("A");
    }else if(score >= 80 && score < 90){
        printf("B");
    }else if(score >= 70 && score < 80){
        printf("C");
    }else if(score >= 60 && score < 70){
        printf("D");
    }else{
        printf("F");
    }
    
    
    return 0;
}