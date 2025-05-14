// Lab 12 - implement top-down parsing for a given Grammar

#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Implementation of a top-down parser
// This is essentially a recursive descent parser
char input[100];
int pos = 0;

void error() {
    printf("\nSyntax Error!\n");
}

char next_token() {
    return input[pos++];
}

// Forward declarations
int expr();
int term();
int factor();

// Parse expression: expr -> term {+ term}
int expr() {
    int result = term();

    while(input[pos] == '+') {
        pos++;  // Consume '+'
        result += term();
    }

    return result;
}

// Parse term: term -> factor {* factor}
int term() {
    int result = factor();

    while(input[pos] == '*') {
        pos++;  // Consume '*'
        result *= factor();
    }

    return result;
}

// Parse factor: factor -> (expr) | number
int factor() {
    int result;

    if(input[pos] == '(') {
        pos++;  // Consume '('
        result = expr();

        if(input[pos] == ')')
            pos++;  // Consume ')'
        else
            error();
    }
    else if(isdigit(input[pos])) {
        result = input[pos] - '0';
        pos++;  // Consume digit
    }
    else {
        error();
        return 0;
    }

    return result;
}

void main() {
    printf("Enter an arithmetic expression (use digits 0-9 and operators +, *): ");
    scanf("%s", input);

    int result = expr();

    if(input[pos] == '\0')
        printf("\nParsing successful! Result = %d\n", result);
    else
        error();
}
