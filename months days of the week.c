#include <stdio.h>

int main() {
    int mid[] = {0, 31, 29, 30, 31, 30, 31, 31, 31, 30, 31, 30, 31};
    int day;
    int month;
    
    // Input the month and day in the format MM/DD
    scanf("%d/%d", &month, &day);
    
    int tm = 0;

    // Add up the days of the months before the current month
    for (int i = 1; i < month; i++) {
        tm += mid[i];
    }
    
    // Add the days of the current month
    int total = tm + day;
  
    if(day < 1 || day > mid[month] || month < 0 || month > 12){
        printf("Invalid Input");
    }else{
  
    int dow = total % 7;
    
    switch(dow){
        case 0: printf("Sunday"); break;
        case 1: printf("Monday"); break;
        case 2: printf("Tuesday"); break;
        case 3: printf("Wednesday"); break;
        case 4: printf("Thursday"); break;
        case 5: printf("Friday"); break;
        case 6: printf("Saturday"); break;

    }
    }
    return 0;

}
