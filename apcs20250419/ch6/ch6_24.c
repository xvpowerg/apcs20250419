/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

int gcd1(int m,int n){
    if (n == 0){
        return m;
    }else{
        return gcd1(n,m%n); 
    }
}
int main()
{  int ans = gcd1(20,14);
    printf("ans:%d",ans);
    return 0;
}