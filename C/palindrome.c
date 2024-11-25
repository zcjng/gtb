#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main() {
    
    char string[1000];
    
    scanf("%s", &string);
    
    bool isPalindrome(char string[]){
        int length = strlen(string);
        int mid = strlen(string) / 2;
        for(int i = 0; i < mid; i++){
            if (string[i] != string[length - i - 1]){
                return false;
            }
        
        }
        return true;
    } 
    
    if (isPalindrome(string)){
        printf("It is a palindrome");
    }
    else{
        printf("It is not a palindrome");
    }
    
    
    return 0;
}

