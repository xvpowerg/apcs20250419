/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

int fit(int n){
    if (n == 1){
        return 1;
    }else{
        return n * fit(n-1);
    }
}
int forLoopFit(int n){
    int ans = 1;
    int i =1;
    for (;i<=n;i++){
        ans *=i;
    }
    return ans;
}
int main()
{   int ans = fit(5);
    printf("ans:%d \n",ans);
    int ans2 = forLoopFit(5);
    printf("ans2:%d",ans2);
    return 0;
}