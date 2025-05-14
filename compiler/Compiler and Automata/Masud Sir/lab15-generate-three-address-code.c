// Lab 15 - generate the three-address code from a source-language expression

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int temp_count = 1;

// Function to generate a new temporary variable
char* new_temp() {
    char* temp = (char*)malloc(10);
    sprintf(temp, "t%d", temp_count++);
    return temp;
}

// Function to trim spaces from a string
void trim_spaces(char* str) {
    char* i = str;
    char* j = str;
    while(*j != 0) {
        *i = *j++;
        if(*i != ' ')
            i++;
    }
    *i = 0;
}

// Function to generate three-address code from an expression
// Returns the temporary variable or variable name holding the result
char* generate_three_address_code(char* expr) {
    char* result = (char*)malloc(50);
    trim_spaces(expr);

    // Handle parentheses by recursion
    int len = strlen(expr);
    if(expr[0] == '(' && expr[len-1] == ')') {
        expr[len-1] = '\0';
        return generate_three_address_code(expr+1);
    }

    // Operator precedence: + and - lowest, * and / higher
    // Scan for + or - outside parentheses
    int paren_count = 0;
    for(int i = len-1; i >= 0; i--) {
        if(expr[i] == ')') paren_count++;
        else if(expr[i] == '(') paren_count--;
        else if(paren_count == 0 && (expr[i] == '+' || expr[i] == '-')) {
            char* left = (char*)malloc(50);
            char* right = (char*)malloc(50);

            strncpy(left, expr, i);
            left[i] = '\0';
            strcpy(right, expr+i+1);

            char* left_var = generate_three_address_code(left);
            char* right_var = generate_three_address_code(right);

            char* temp_var = new_temp();
            printf("%s = %s %c %s\n", temp_var, left_var, expr[i], right_var);
            strcpy(result, temp_var);

            free(left);
            free(right);
            free(left_var);
            free(right_var);
            free(temp_var);

            return result;
        }
    }

    // Scan for * or / outside parentheses
    paren_count = 0;
    for(int i = len-1; i >= 0; i--) {
        if(expr[i] == ')') paren_count++;
        else if(expr[i] == '(') paren_count--;
        else if(paren_count == 0 && (expr[i] == '*' || expr[i] == '/')) {
            char* left = (char*)malloc(50);
            char* right = (char*)malloc(50);

            strncpy(left, expr, i);
            left[i] = '\0';
            strcpy(right, expr+i+1);

            char* left_var = generate_three_address_code(left);
            char* right_var = generate_three_address_code(right);

            char* temp_var = new_temp();
            printf("%s = %s %c %s\n", temp_var, left_var, expr[i], right_var);
            strcpy(result, temp_var);

            free(left);
            free(right);
            free(left_var);
            free(right_var);
            free(temp_var);

            return result;
        }
    }

    // If no operator found, it is a variable or number
    strcpy(result, expr);
    return result;
}

int main() {
    char expression[100];

    printf("Enter an expression: ");
    if(fgets(expression, sizeof(expression), stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return 1;
    }

    // Remove trailing newline if present
    size_t len = strlen(expression);
    if(len > 0 && expression[len-1] == '\n') {
        expression[len-1] = '\0';
    }

    char* assign_pos = strchr(expression, '=');
    if(assign_pos != NULL) {
        // Assignment expression
        char* left_side = (char*)malloc(50);
        char* right_side = (char*)malloc(50);

        int assign_index = assign_pos - expression;
        strncpy(left_side, expression, assign_index);
        left_side[assign_index] = '\0';
        strcpy(right_side, assign_pos + 1);

        char* right_var = generate_three_address_code(right_side);
        printf("%s = %s\n", left_side, right_var);

        free(left_side);
        free(right_side);
        free(right_var);
    } else {
        char* result = generate_three_address_code(expression);
        free(result);
    }

    return 0;
}

//a+(b-c)*d