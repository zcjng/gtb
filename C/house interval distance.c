#include <stdio.h>

int diff(int arr[], int n){
    int min_sel = 1000000;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
        int diff = arr[i] - arr[j];
        if(diff < 0) diff = -diff;
        
        if(diff < min_sel){
            min_sel = diff;
            }
        }
    }
        return min_sel;
}

int main(void){
    int n;
    scanf("%d", &n);
    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    int k;
    scanf("%d", &k);
    int arr2[k];
    for(int i = 0; i < k; i++){
        scanf("%d", &arr2[i]);
    }
    int m;
    scanf("%d", &m);
    int arr3[m];
    for(int i = 0; i < m; i++){
        scanf("%d", &arr3[i]);
    }
    printf("%d\n", diff(arr, n));
    printf("%d\n", diff(arr2, k));
    printf("%d\n", diff(arr3, m));
    

    return 0;
}
