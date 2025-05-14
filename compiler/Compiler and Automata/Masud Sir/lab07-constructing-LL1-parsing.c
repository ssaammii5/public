//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_PROD 20
#define MAX_LEN 50
#define MAX_NON_TERMINALS 10
#define MAX_TERMINALS 10

// Structure to store grammar productions
typedef struct {
    char lhs;
    char rhs[MAX_LEN];
} Production;

// Global variables
Production productions[MAX_PROD];
int num_productions = 0;
char non_terminals[MAX_NON_TERMINALS];
char terminals[MAX_TERMINALS];
int num_non_terminals = 0;
int num_terminals = 0;
char first[MAX_NON_TERMINALS][MAX_TERMINALS];
char follow[MAX_NON_TERMINALS][MAX_TERMINALS];
char parsing_table[MAX_NON_TERMINALS][MAX_TERMINALS][MAX_LEN];

// Function to check if a character is a non-terminal
int is_non_terminal(char c) {
    return isupper(c);
}

// Function to add a character to an array if not already present
void add_if_not_present(char *arr, int *size, char c) {
    for (int i = 0; i < *size; i++) {
        if (arr[i] == c) return;
    }
    arr[(*size)++] = c;
}

// Function to get index of a non-terminal
int get_non_terminal_index(char nt) {
    for (int i = 0; i < num_non_terminals; i++) {
        if (non_terminals[i] == nt) return i;
    }
    return -1;
}

// Function to get index of a terminal
int get_terminal_index(char t) {
    for (int i = 0; i < num_terminals; i++) {
        if (terminals[i] == t) return i;
    }
    return -1;
}

// Function to compute FIRST sets
void compute_first() {
    int changed;

    // Initialize FIRST sets
    for (int i = 0; i < num_non_terminals; i++) {
        for (int j = 0; j < num_terminals; j++) {
            first[i][j] = 0;
        }
    }

    do {
        changed = 0;

        for (int i = 0; i < num_productions; i++) {
            char lhs = productions[i].lhs;
            char *rhs = productions[i].rhs;
            int lhs_index = get_non_terminal_index(lhs);

            if (rhs[0] == '#') { // Epsilon production
                int eps_index = get_terminal_index('#');
                if (eps_index != -1 && !first[lhs_index][eps_index]) {
                    first[lhs_index][eps_index] = 1;
                    changed = 1;
                }
            } else if (!is_non_terminal(rhs[0])) { // Terminal
                int term_index = get_terminal_index(rhs[0]);
                if (term_index != -1 && !first[lhs_index][term_index]) {
                    first[lhs_index][term_index] = 1;
                    changed = 1;
                }
            } else { // Non-terminal
                int k = 0;
                int can_derive_epsilon = 1;

                while (rhs[k] != '\0' && can_derive_epsilon) {
                    if (!is_non_terminal(rhs[k])) {
                        int term_index = get_terminal_index(rhs[k]);
                        if (term_index != -1 && !first[lhs_index][term_index]) {
                            first[lhs_index][term_index] = 1;
                            changed = 1;
                        }
                        can_derive_epsilon = 0;
                    } else {
                        int nt_index = get_non_terminal_index(rhs[k]);
                        int eps_index = get_terminal_index('#');

                        for (int j = 0; j < num_terminals; j++) {
                            if (j != eps_index && first[nt_index][j] && !first[lhs_index][j]) {
                                first[lhs_index][j] = 1;
                                changed = 1;
                            }
                        }

                        if (eps_index == -1 || !first[nt_index][eps_index]) {
                            can_derive_epsilon = 0;
                        }
                    }
                    k++;
                }

                if (can_derive_epsilon) {
                    int eps_index = get_terminal_index('#');
                    if (eps_index != -1 && !first[lhs_index][eps_index]) {
                        first[lhs_index][eps_index] = 1;
                        changed = 1;
                    }
                }
            }
        }
    } while (changed);
}

// Function to compute FOLLOW sets
void compute_follow() {
    int changed;
    int start_symbol_index = get_non_terminal_index(productions[0].lhs);
    int dollar_index = get_terminal_index('$');

    // Initialize FOLLOW sets
    for (int i = 0; i < num_non_terminals; i++) {
        for (int j = 0; j < num_terminals; j++) {
            follow[i][j] = 0;
        }
    }

    // Add $ to FOLLOW of start symbol
    if (dollar_index != -1) {
        follow[start_symbol_index][dollar_index] = 1;
    }

    do {
        changed = 0;

        for (int i = 0; i < num_productions; i++) {
            char *rhs = productions[i].rhs;
            int len = strlen(rhs);

            for (int j = 0; j < len; j++) {
                if (is_non_terminal(rhs[j])) {
                    int nt_index = get_non_terminal_index(rhs[j]);

                    if (j == len - 1) { // B -> αA
                        int lhs_index = get_non_terminal_index(productions[i].lhs);
                        for (int k = 0; k < num_terminals; k++) {
                            if (follow[lhs_index][k] && !follow[nt_index][k]) {
                                follow[nt_index][k] = 1;
                                changed = 1;
                            }
                        }
                    } else if (!is_non_terminal(rhs[j+1])) { // B -> αAaβ
                        int term_index = get_terminal_index(rhs[j+1]);
                        if (term_index != -1 && !follow[nt_index][term_index] && rhs[j+1] != '#') {
                            follow[nt_index][term_index] = 1;
                            changed = 1;
                        }
                    } else { // B -> αACβ
                        int next_nt_index = get_non_terminal_index(rhs[j+1]);
                        int eps_index = get_terminal_index('#');

                        for (int k = 0; k < num_terminals; k++) {
                            if (k != eps_index && first[next_nt_index][k] && !follow[nt_index][k]) {
                                follow[nt_index][k] = 1;
                                changed = 1;
                            }
                        }

                        if (eps_index != -1 && first[next_nt_index][eps_index]) {
                            int lhs_index = get_non_terminal_index(productions[i].lhs);
                            for (int k = 0; k < num_terminals; k++) {
                                if (follow[lhs_index][k] && !follow[nt_index][k]) {
                                    follow[nt_index][k] = 1;
                                    changed = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    } while (changed);
}

// Function to construct the LL(1) parsing table
void construct_parsing_table() {
    // Initialize parsing table
    for (int i = 0; i < num_non_terminals; i++) {
        for (int j = 0; j < num_terminals; j++) {
            parsing_table[i][j][0] = '\0';
        }
    }

    for (int i = 0; i < num_productions; i++) {
        char lhs = productions[i].lhs;
        char *rhs = productions[i].rhs;
        int lhs_index = get_non_terminal_index(lhs);

        if (rhs[0] == '#') { // A -> ε
            int eps_index = get_terminal_index('#');
            for (int j = 0; j < num_terminals; j++) {
                if (follow[lhs_index][j]) {
                    strcat(parsing_table[lhs_index][j], "#");
                }
            }
        } else {
            int first_char_index;
            if (!is_non_terminal(rhs[0])) {
                first_char_index = get_terminal_index(rhs[0]);
                if (first_char_index != -1 && rhs[0] != '#') {
                    strcpy(parsing_table[lhs_index][first_char_index], rhs);
                }
            } else {
                int nt_index = get_non_terminal_index(rhs[0]);
                for (int j = 0; j < num_terminals; j++) {
                    if (first[nt_index][j]) {
                        strcpy(parsing_table[lhs_index][j], rhs);
                    }
                }
            }
        }
    }
}

// Function to print the LL(1) parsing table
void print_parsing_table() {
    printf("\nLL(1) Parsing Table:\n");
    printf("------------------------------------------------------\n");
    printf("   | ");
    for (int i = 0; i < num_terminals; i++) {
        printf("%c | ", terminals[i]);
    }
    printf("\n------------------------------------------------------\n");

    for (int i = 0; i < num_non_terminals; i++) {
        printf(" %c | ", non_terminals[i]);
        for (int j = 0; j < num_terminals; j++) {
            if (parsing_table[i][j][0] != '\0') {
                printf("%c->%s | ", non_terminals[i], parsing_table[i][j]);
            } else {
                printf("     | ");
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------\n");
}

// Function to parse an input string
void parse_input(char *input) {
    char stack[100];
    int top = -1;
    int input_pos = 0;

    // Initialize stack with $ and start symbol
    stack[++top] = '$';
    stack[++top] = productions[0].lhs;

    printf("\nParsing Input: %s\n", input);
    printf("------------------------------------------------------\n");
    printf("Stack\t\tInput\t\tAction\n");
    printf("------------------------------------------------------\n");

    while (top >= 0) {
        // Print current stack and input
        printf("$");
        for (int i = 0; i <= top; i++) {
            printf("%c", stack[i]);
        }
        printf("\t\t");

        for (int i = input_pos; i < strlen(input); i++) {
            printf("%c", input[i]);
        }
        printf("\t\t");

        char stack_top = stack[top];
        char current_input = input[input_pos];

        if (!is_non_terminal(stack_top)) {
            if (stack_top == current_input) {
                printf("Match %c\n", stack_top);
                top--;
                input_pos++;
            } else {
                printf("Error: Expected %c, got %c\n", stack_top, current_input);
                return;
            }
        } else {
            int nt_index = get_non_terminal_index(stack_top);
            int term_index = get_terminal_index(current_input);

            if (term_index != -1 && parsing_table[nt_index][term_index][0] != '\0') {
                char *production = parsing_table[nt_index][term_index];
                printf("Apply %c -> %s\n", stack_top, production);

                top--; // Pop the non-terminal

                // Push the production in reverse order
                if (strcmp(production, "#") != 0) { // Skip if epsilon
                    int prod_len = strlen(production);
                    for (int i = prod_len - 1; i >= 0; i--) {
                        stack[++top] = production[i];
                    }
                }
            } else {
                printf("Error: No production for %c with lookahead %c\n", stack_top, current_input);
                return;
            }
        }
    }

    if (input_pos == strlen(input)) {
        printf("------------------------------------------------------\n");
        printf("Input accepted!\n");
    } else {
        printf("------------------------------------------------------\n");
        printf("Error: Input not fully consumed\n");
    }
}

// Function to initialize the grammar with predefined productions
void initialize_grammar() {
    // Set the number of productions
    num_productions = 8;

    // Define the productions
    productions[0].lhs = 'E';
    strcpy(productions[0].rhs, "TR");

    productions[1].lhs = 'R';
    strcpy(productions[1].rhs, "+TR");

    productions[2].lhs = 'R';
    strcpy(productions[2].rhs, "#");

    productions[3].lhs = 'T';
    strcpy(productions[3].rhs, "FY");

    productions[4].lhs = 'Y';
    strcpy(productions[4].rhs, "*FY");

    productions[5].lhs = 'Y';
    strcpy(productions[5].rhs, "#");

    productions[6].lhs = 'F';
    strcpy(productions[6].rhs, "(E)");

    productions[7].lhs = 'F';
    strcpy(productions[7].rhs, "i");

    // Add non-terminals and terminals to the lists
    for (int i = 0; i < num_productions; i++) {
        // Add non-terminal to the list
        add_if_not_present(non_terminals, &num_non_terminals, productions[i].lhs);

        // Add terminals and non-terminals from RHS
        for (int j = 0; productions[i].rhs[j] != '\0'; j++) {
            char c = productions[i].rhs[j];
            if (is_non_terminal(c)) {
                add_if_not_present(non_terminals, &num_non_terminals, c);
            } else {
                add_if_not_present(terminals, &num_terminals, c);
            }
        }
    }

    // Add $ as a terminal
    add_if_not_present(terminals, &num_terminals, '$');
}

int main() {
    printf("LL(1) Parser Construction\n");
    printf("=========================\n");

    // Initialize grammar with predefined productions
    initialize_grammar();

    // Print the productions
    printf("Productions:\n");
    for (int i = 0; i < num_productions; i++) {
        printf("Production %d: %c=%s\n", i+1, productions[i].lhs, productions[i].rhs);
    }

    // Compute FIRST and FOLLOW sets
    compute_first();
    compute_follow();

    // Print FIRST sets
    printf("\nFIRST sets:\n");
    for (int i = 0; i < num_non_terminals; i++) {
        printf("FIRST(%c) = { ", non_terminals[i]);
        for (int j = 0; j < num_terminals; j++) {
            if (first[i][j]) {
                printf("%c ", terminals[j]);
            }
        }
        printf("}\n");
    }

    // Print FOLLOW sets
    printf("\nFOLLOW sets:\n");
    for (int i = 0; i < num_non_terminals; i++) {
        printf("FOLLOW(%c) = { ", non_terminals[i]);
        for (int j = 0; j < num_terminals; j++) {
            if (follow[i][j]) {
                printf("%c ", terminals[j]);
            }
        }
        printf("}\n");
    }

    // Construct and print parsing table
    construct_parsing_table();
    print_parsing_table();

    // Parse input string
    char input[] = "i+i*i$";
    parse_input(input);

    return 0;
}
