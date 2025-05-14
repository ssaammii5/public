// Lab 06 - Simulate lexical analyzer for validating operators

#include <stdio.h>
#include <string.h>

int is_operator(char c) {
    char operators[] = "+-*/%=<>&|!^~?:";
    for(int i = 0; i < strlen(operators); i++) {
        if(c == operators[i])
            return 1;
    }
    return 0;
}

void main() {
    char expression[100];
    int operator_count = 0;

    printf("Enter an expression: ");
    gets(expression);

    printf("\nOperators found:\n");
    for(int i = 0; i < strlen(expression); i++) {
        if(is_operator(expression[i])) {
            printf("%c at position %d\n", expression[i], i+1);
            operator_count++;

            // Check for compound operators
            if((expression[i] == '+' && expression[i+1] == '+') ||
               (expression[i] == '-' && expression[i+1] == '-') ||
               (expression[i] == '=' && expression[i+1] == '=') ||
               (expression[i] == '!' && expression[i+1] == '=') ||
               (expression[i] == '>' && expression[i+1] == '=') ||
               (expression[i] == '<' && expression[i+1] == '=')) {
                printf("%c%c at position %d (compound operator)\n",
                       expression[i], expression[i+1], i+1);
                i++;  // Skip the next character as it's part of this operator
               }
        }
    }

    printf("\nTotal operators found: %d\n", operator_count);
}
