        #include <stdio.h>

int main(){     //NESTED CONDITION STATEMENTS 3
    unsigned int counter;
    int grade, passed, failed;
    passed = 0;
    failed = 0;
    
    counter = 1;
    while(counter <= 10){
    
    printf("Input the grade = ");
    scanf("%d", &grade);
    counter++;
    
    if (grade >= 70)
        passed++;
    else
        failed++;
}
    if (passed >= 8){
        printf("%d Passed \n%d Failed\n", passed, failed);
        printf("Bonus to the instructor!");
    }
    else{
        printf("%d Passed \n%d Failed\n", passed, failed);
        puts("No bonus");
    }
}
