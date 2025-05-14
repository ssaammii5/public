// Lab 08 - implementing predictive parser for a mini language

#include <stdio.h>
#include <string.h>

// Predictive parser for a mini language
// Non-terminals: S, A, B, C
// Terminals: a, b, c, d

/*
S → A
A → Bb | Cd
B → aB | ε
C → Cc | ε
 */


char table[4][5][10] = {
    // S            a       b       c       d       $
    {"A",          "A",    "A",    "A",    "A",    ""},
    // A            a       b       c       d       $
    {"Bb",         "Bb",   "Bb",   "Cd",   "Cd",   ""},
    // B            a       b       c       d       $
    {"aB",         "@",    "@",    "@",    "@",    "@"},
    // C            a       b       c       d       $
    {"@",          "@",    "@",    "Cc",   "@",    "@"}
};

char stack[100];
char input[100]; // Just declare the array, we'll fill it in main
int top = -1;
int ip = 0;

char pop() {
    if(top == -1) return -1;
    return stack[top--];
}

void push(char c) {
    stack[++top] = c;
}

int get_non_terminal_index(char c) {
    switch(c) {
        case 'S': return 0;
        case 'A': return 1;
        case 'B': return 2;
        case 'C': return 3;
        default: return -1;
    }
}

int get_terminal_index(char c) {
    switch(c) {
        case 'a': return 0;
        case 'b': return 1;
        case 'c': return 2;
        case 'd': return 3;
        case '$': return 4;
        default: return -1;
    }
}

void parse() {
    push('$');
    push('S');

    int accepted = 0;  // Flag to track if input is accepted

    printf("\nStack\tInput\tAction\n");

    while(top != -1) {
        // Print current stack and remaining input
        printf("\n");
        for(int i = top; i >= 0; i--)
            printf("%c", stack[i]);
        printf("\t%s\t", &input[ip]);

        // If top of stack is same as current input symbol, match and advance
        if(stack[top] == input[ip]) {
            printf("Match %c", input[ip]);

            // Check if we've matched the end marker and the stack will be empty
            if(input[ip] == '$' && top == 0) {
                accepted = 1;
            }

            pop();
            ip++;
            continue;
        }

        // If epsilon production (@)
        if(stack[top] == '@') {
            printf("Pop @");
            pop();
            continue;
        }

        // Lookup in parse table
        int row = get_non_terminal_index(stack[top]);
        int col = get_terminal_index(input[ip]);

        if(row == -1 || col == -1 || table[row][col][0] == '\0') {
            printf("Error: No production found for %c with lookahead %c", stack[top], input[ip]);
            accepted = 0;
            break;
        }

        // Production found, replace stack top
        printf("Apply %c -> %s", stack[top], table[row][col]);
        pop(); // Remove the non-terminal from stack

        // Push production in reverse order
        for(int i = strlen(table[row][col])-1; i >= 0; i--) {
            push(table[row][col][i]);
        }
    }

    if(accepted)
        printf("\n\nInput string accepted!\n");
    else
        printf("\n\nError: Parsing failed!\n");
}

int main() {
    printf("Enter input string ending with $: ");
    scanf("%s", input);

    // Reset the input pointer for parse
    ip = 0;
    top = -1; // Reset stack

    printf("Parsing input string: %s\n", input);
    parse();

    return 0;
}

/*
 * Valid inputs:
 * b$
 * ab$
 * aab$
 * aaab$
 * d$
 * cd$
 * ccd$
 * cccd$
 */
