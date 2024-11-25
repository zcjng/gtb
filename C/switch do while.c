#include <stdio.h>
#include <math.h>

void fx(){

    double principal, interest, result;
    principal = 1000;
    interest = .05;
    unsigned int years;
    
    printf("%4s%21s\n", "Year", "Amount of Deposit"); //Deposit thing, kinda weird but alright since it uses for loop.  //The interest grow 1.0 every year and to the yearsth 

    for(years = 1; years <= 10; years++){
        result = principal * pow(1.0 + interest, years);
    
        printf("%4u%21.0f\n", years, result);
    }
    
    
}

#include <stdio.h>
#include <ctype.h>

void fx2(){
    int grade;
    unsigned int acounter = 0;
    unsigned int bcounter = 0;
    unsigned int ccounter = 0;
    unsigned int dcounter = 0;
    
    puts("Enter a grade =");
    while( (grade = getchar()) != EOF ){
        grade = toupper(grade);
        
        switch(grade){
            case 'A':
                acounter++;
                break;
            case 'B':
                bcounter++;
                break;
            case 'C':
                ccounter++;
                break;
            case 'D':
                dcounter++;
                break;
            case '\n':
            case '\t':
            case ' ':
                break;
            default:
                puts("Please enter a valid character");
                break;
            
        }
    }
        puts("The total grades this year\n");
        printf("Grade A = %u\n", acounter);
        printf("Grade B = %u\n", bcounter);
        printf("Grade C = %u\n", ccounter);
        printf("Grade D = %u\n", dcounter);
        
    
    
}


#include <stdio.h>
#include <ctype.h>

void f3(){
    
    int i = 50;
    do{
        printf("We have to do this!\n");        //Do while statements.
        i += 5;                         //The difference is that, the loop condition will be executed 1 time just before the condition gets checked.
    }while(i < 100);
    
    printf("%u", i);
        

}

#include <stdio.h>
#include <ctype.h>

int main() {
    int i = 50;
    
    do {
        if (i == 70) {
            i += 5;  // Increment before continue to avoid infinite loop
            continue;
        }
        printf("%u\n", i);
        i += 5;
    } while (i <= 70);
    
    printf("%u", i);
    
    return 0;
}
