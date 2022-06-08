#include<stdio.h>
int dp[100][100];
#define INT_MAX 1e5
int min(int a,int b){
    if (a<b) return a;
    return b;
}

int matrix_chain(int arr[],int i,int j){
    if(i==j){
        return 0;
    }
    if(dp[i][j]!=-1) return dp[i][j];

    dp[i][j]=INT_MAX;
    for(int k=i;k<j;k++){

        dp[i][j]=min(dp[i][j],matrix_chain(arr,i,k)+matrix_chain(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]);
    }
    return dp[i][j];
}
int main(){
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    
    for(int i=0;i<100;i++){
        for(int j=0;j<100;j++){
            dp[i][j]=-1;
        }
    }
    int ans=matrix_chain(arr,1,n-1);
    printf("%d ",ans);
}