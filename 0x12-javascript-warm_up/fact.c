#include <stdio.h>
#include<stdlib.h>

int factorial(int n)
{
    if (n < 0) { // Check if firstArg is negative
        return 0; // Return 'NaN' if firstArg is negative
    }

    int result = 1;
    int i;
    for (i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main(int arg, char **argv)
{
    if (arg != 2)
    {
        printf("Usage: %s <number>\n", argv[0]);
    } 
    int firstArg = atoi(argv[1]);
    int result =  factorial(firstArg);
    printf("Factorial of %d is %d\n", firstArg, result);
    
    return 0;
}
