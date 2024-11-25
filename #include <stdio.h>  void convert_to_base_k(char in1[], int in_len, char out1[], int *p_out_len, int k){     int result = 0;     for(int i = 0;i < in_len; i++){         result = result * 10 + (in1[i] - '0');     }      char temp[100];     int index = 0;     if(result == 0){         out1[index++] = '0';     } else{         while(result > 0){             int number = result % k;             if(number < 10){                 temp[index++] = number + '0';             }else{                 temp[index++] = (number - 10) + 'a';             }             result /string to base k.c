#include <stdio.h>

void convert_to_base_k(char in1[], int in_len, char out1[], int *p_out_len, int k){
    int result = 0;
    for(int i = 0;i < in_len; i++){
        result = result * 10 + (in1[i] - '0');
    }

    char temp[100];
    int index = 0;
    if(result == 0){
        out1[index++] = '0';
    } else{
        while(result > 0){
            int number = result % k;
            if(number < 10){
                temp[index++] = number + '0';
            }else{
                temp[index++] = (number - 10) + 'a';
            }
            result /= k;
        }
    }
    for(int i = 0; i < index; i++){
        out1[i] = temp[index - i - 1];
    }
    *p_out_len = index;
    out1[index] = '\0';
}

int main(void){
    int len;
    scanf("%d", &len);
    char input[len + 1];
    scanf("%s", input);
    int k;
    scanf("%d", &k);

    char output[1000];
    int out_len;
    convert_to_base_k(input, len, output, &out_len, k);

    printf("%s\n", output);

    return 0;
}
