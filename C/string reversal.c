#include <stdio.h>
#include <string.h> /*REVERSE STRINGS*/

void input(int *n, char string[]){
    scanf("%s", string);
    *n = strlen(string);
}

void reverse(int n, char string[]){
    for(int i = 0; i < n / 2; i++){
        char temp = string[i];
        string[i] = string[n - i - 1];
        string[n - i - 1] = temp;
    }
}

void output(int n, char string[]){
    printf("%s\n", string);
}
int main() {
    int n;
    char string[1000];
    
    input(&n, string);
    reverse(n, string);
    output(n, string);
    return 0;
}
