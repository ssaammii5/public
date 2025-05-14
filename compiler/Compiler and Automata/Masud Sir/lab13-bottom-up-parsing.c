// Lab 13 - implement bottom-up parsing for a given Grammar

#include <stdio.h>
#include <string.h>

// Bottom-up LR(0) parsing for a simple grammar
// E -> E + T | T
// T -> T * F | F
// F -> ( E ) | id

// Represents the parse stack
char stack[100];
int top = -1;

// Push operation for stack
void push(char c) {
    stack[++top] = c;
}

// Pop operation for stack
char pop() {
    return stack[top--];
}

// Function to check if a reduction is possible
int can_reduce(int start_pos, int end_pos, char *to) {
    // Check different reduction possibilities
    // For simplicity, we'll check a few common reductions

    // F -> id
    if(end_pos - start_pos == 0 && stack[start_pos] == 'i') {
        *to = 'F';
        return 1;
    }

    // F -> ( E )
    if(end_pos - start_pos == 2 && stack[start_pos] == '(' &&
       stack[start_pos+1] == 'E' && stack[end_pos] == ')') {
        *to = 'F';
        return 1;
    }

    // T -> F
    if(end_pos - start_pos == 0 && stack[start_pos] == 'F') {
        *to = 'T';
        return 1;
    }

    // T -> T * F
    if(end_pos - start_pos == 2 && stack[start_pos] == 'T' &&
       stack[start_pos+1] == '*' && stack[end_pos] == 'F') {
        *to = 'T';
        return 1;
    }

    // E -> T
    if(end_pos - start_pos == 0 && stack[start_pos] == 'T') {
        *to = 'E';
        return 1;
    }

    // E -> E + T
    if(end_pos - start_pos == 2 && stack[start_pos] == 'E' &&
       stack[start_pos+1] == '+' && stack[end_pos] == 'T') {
        *to = 'E';
        return 1;
    }

    return 0;
}

// Function to perform reductions
void reduce() {
    int reduced = 1;

    while(reduced) {
        reduced = 0;

        // Try different reduction possibilities
        for(int i = 0; i <= top; i++) {
            for(int j = i; j <= top; j++) {
                char to;
                if(can_reduce(i, j, &to)) {
                    // Perform the reduction
                    int len = j - i + 1;

                    printf("Reduce: ");
                    for(int k = i; k <= j; k++)
                        printf("%c", stack[k]);
                    printf(" to %c\n", to);

                    // Remove the production body
                    top -= len;

                    // Insert the production head
                    push(to);

                    reduced = 1;
                    break;
                }
            }
            if(reduced) break;
        }
    }
}

// The parsing function
void parse(char *input) {
    int i = 0;

    printf("Shift-Reduce Parsing Actions:\n");

    while(input[i] != '\0') {
        // Shift the current input symbol
        printf("Shift: %c\n", input[i]);
        push(input[i]);
        i++;

        // Try to reduce
        reduce();

        // Print current stack
        printf("Stack: ");
        for(int j = 0; j <= top; j++)
            printf("%c", stack[j]);
        printf("\n\n");
    }

    // Final reductions if needed
    reduce();

    // Check if parsing is successful
    if(top == 0 && stack[top] == 'E')
        printf("\nParsing Successful!\n");
    else
        printf("\nParsing Failed!\n");
}

void main() {
    char input[100];

    printf("Enter input string (use 'i' for id): ");
    scanf("%s", input);

    parse(input);
}
