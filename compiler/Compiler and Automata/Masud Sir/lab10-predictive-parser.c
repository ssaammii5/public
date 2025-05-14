// Lab 10 - Design a Predictive Parser for the specified grammar

#include <stdio.h>
#include <string.h>

// Parsing table for the grammar:
// E -> TE'
// E' -> +TE' | ε
// T -> FT'
// T' -> *FT' | ε
// F -> (E) | id

char table[5][6][10] = {
    // E row (id, (, ), +, *, $)
    {"TE'", "TE'", "", "", "", ""},

    // E' row
    {"", "", "ε", "+TE'", "", "ε"},

    // T row
    {"FT'", "FT'", "", "", "", ""},

    // T' row
    {"", "", "ε", "ε", "*FT'", "ε"},

    // F row
    {"id", "(E)", "", "", "", ""}
};

char stack[100];
char input[100];
int top = -1;
int ip = 0;

char pop() {
    return stack[top--];
}

void push(char c) {
    stack[++top] = c;
}

int get_non_terminal_index(char c) {
    switch(c) {
        case 'E': return 0;
        case 'A': return 1; // For E'
        case 'T': return 2;
        case 'B': return 3; // For T'
        case 'F': return 4;
        default: return -1;
    }
}

int get_terminal_index(char c) {
    switch(c) {
        case 'i': return 0; // For id
        case '(': return 1;
        case ')': return 2;
        case '+': return 3;
        case '*': return 4;
        case '$': return 5;
        default: return -1;
    }
}

void parse() {
    push('$');
    push('E');

    printf("\nStack\tInput\tAction\n");

    while(top != -1) {
        // Print current stack and remaining input
        printf("\n");
        for(int i = 0; i <= top; i++)
            printf("%c", stack[i]);
        printf("\t%s\t", &input[ip]);

        // If top of stack is same as current input symbol, match and advance
        if(stack[top] == input[ip]) {
            printf("Match %c", input[ip]);
            pop();
            ip++;
            continue;
        }

        // If epsilon production (ε)
        if(stack[top] == 'ε') {
            printf("Pop ε");
            pop();
            continue;
        }

        // Lookup in parse table
        int row = get_non_terminal_index(stack[top]);
        int col = get_terminal_index(input[ip]);

        if(row == -1 || col == -1 || table[row][col][0] == '\0') {
            printf("Error: No production found");
            return;
        }

        // Production found, replace stack top
        printf("Apply %c -> %s", stack[top], table[row][col]);
        char top_symbol = pop();

        // Push production in reverse order
        for(int i = strlen(table[row][col])-1; i >= 0; i--) {
            push(table[row][col][i]);
        }
    }

    if(input[ip] == '$')
        printf("\n\nInput string accepted!\n");
    else
        printf("\n\nError: Parsing failed!\n");
}

void main() {
    printf("Enter input string ending with $ (use i for id): ");
    scanf("%s", input);

    parse();
}
