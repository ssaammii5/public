// Lab 11 - Calculate First and Follow sets of given grammar

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAX_PROD 20
#define MAX_LEN 20

// Structure to store grammar productions
typedef struct {
    char left;
    char right[MAX_LEN];
} Production;

Production productions[MAX_PROD];
int num_productions = 0;

// Arrays to store FIRST and FOLLOW sets
char first[26][MAX_LEN];
char follow[26][MAX_LEN];

// Function to check if character exists in string
int exists(char *str, char ch) {
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == ch) {
            return 1;
        }
    }
    return 0;
}

// Function to add character to set if not already present
void add_to_set(char *set, char ch) {
    if (!exists(set, ch)) {
        int len = strlen(set);
        set[len] = ch;
        set[len + 1] = '\0';
    }
}

// Function to calculate FIRST set for a symbol or string
void calculate_first(char *result, char *str) {
    // If string is empty, return
    if (strlen(str) == 0) {
        return;
    }

    // If first symbol is terminal, add it to result
    if (!isupper(str[0]) && str[0] != '@') {
        add_to_set(result, str[0]);
        return;
    }

    // If first symbol is epsilon, add it to result
    if (str[0] == '@') {
        add_to_set(result, '@');
        return;
    }

    // If first symbol is non-terminal
    if (isupper(str[0])) {
        // Add all elements from FIRST(first symbol) to result except epsilon
        for (int i = 0; i < strlen(first[str[0] - 'A']); i++) {
            if (first[str[0] - 'A'][i] != '@') {
                add_to_set(result, first[str[0] - 'A'][i]);
            }
        }

        // If epsilon is in FIRST of first symbol and there are more symbols
        if (exists(first[str[0] - 'A'], '@') && strlen(str) > 1) {
            // Calculate FIRST of remaining string
            char temp[MAX_LEN] = "";
            calculate_first(temp, str + 1);

            // Add all elements from FIRST of remaining string to result
            for (int i = 0; i < strlen(temp); i++) {
                add_to_set(result, temp[i]);
            }
        }

        // If all symbols in string can derive epsilon, add epsilon to result
        int all_have_epsilon = 1;
        for (int i = 0; i < strlen(str); i++) {
            if (!isupper(str[i]) || !exists(first[str[i] - 'A'], '@')) {
                all_have_epsilon = 0;
                break;
            }
        }

        if (all_have_epsilon) {
            add_to_set(result, '@');
        }
    }
}

// Function to compute FIRST sets for all non-terminals
void compute_first_sets() {
    int changed;

    // Initialize FIRST sets
    for (int i = 0; i < 26; i++) {
        first[i][0] = '\0';
    }

    do {
        changed = 0;

        // For each production
        for (int i = 0; i < num_productions; i++) {
            char nt = productions[i].left;
            char *rhs = productions[i].right;
            int old_len = strlen(first[nt - 'A']);

            // If RHS starts with epsilon
            if (rhs[0] == '@') {
                if (!exists(first[nt - 'A'], '@')) {
                    add_to_set(first[nt - 'A'], '@');
                    changed = 1;
                }
                continue;
            }

            // If RHS starts with terminal
            if (!isupper(rhs[0])) {
                if (!exists(first[nt - 'A'], rhs[0])) {
                    add_to_set(first[nt - 'A'], rhs[0]);
                    changed = 1;
                }
                continue;
            }

            // If RHS starts with non-terminal
            char temp[MAX_LEN] = "";
            calculate_first(temp, rhs);

            // Add all elements from temp to FIRST(nt)
            for (int j = 0; j < strlen(temp); j++) {
                if (!exists(first[nt - 'A'], temp[j])) {
                    add_to_set(first[nt - 'A'], temp[j]);
                    changed = 1;
                }
            }
        }
    } while (changed);
}

// Function to compute FOLLOW sets for all non-terminals
void compute_follow_sets() {
    int changed;

    // Initialize FOLLOW sets
    for (int i = 0; i < 26; i++) {
        follow[i][0] = '\0';
    }

    // Add $ to FOLLOW of start symbol (first production's left side)
    add_to_set(follow[productions[0].left - 'A'], '$');

    do {
        changed = 0;

        // For each production
        for (int i = 0; i < num_productions; i++) {
            char nt_left = productions[i].left;
            char *rhs = productions[i].right;

            // For each symbol in RHS
            for (int j = 0; j < strlen(rhs); j++) {
                // If symbol is non-terminal
                if (isupper(rhs[j])) {
                    // If it's the last symbol, add FOLLOW(left) to FOLLOW(symbol)
                    if (j == strlen(rhs) - 1) {
                        int old_len = strlen(follow[rhs[j] - 'A']);

                        for (int k = 0; k < strlen(follow[nt_left - 'A']); k++) {
                            add_to_set(follow[rhs[j] - 'A'], follow[nt_left - 'A'][k]);
                        }

                        if (strlen(follow[rhs[j] - 'A']) > old_len) {
                            changed = 1;
                        }
                    }
                    // If not the last symbol
                    else {
                        // Calculate FIRST of remaining string
                        char temp[MAX_LEN] = "";
                        calculate_first(temp, rhs + j + 1);
                        int old_len = strlen(follow[rhs[j] - 'A']);

                        // Add all non-epsilon symbols from FIRST of remaining string to FOLLOW(symbol)
                        for (int k = 0; k < strlen(temp); k++) {
                            if (temp[k] != '@') {
                                add_to_set(follow[rhs[j] - 'A'], temp[k]);
                            }
                        }

                        // If epsilon is in FIRST of remaining string, add FOLLOW(left) to FOLLOW(symbol)
                        if (exists(temp, '@')) {
                            for (int k = 0; k < strlen(follow[nt_left - 'A']); k++) {
                                add_to_set(follow[rhs[j] - 'A'], follow[nt_left - 'A'][k]);
                            }
                        }

                        if (strlen(follow[rhs[j] - 'A']) > old_len) {
                            changed = 1;
                        }
                    }
                }
            }
        }
    } while (changed);
}

int main() {
    // Sample grammar input
    num_productions = 8;

    // E -> TX
    productions[0].left = 'E';
    strcpy(productions[0].right, "TX");

    // X -> +TX
    productions[1].left = 'X';
    strcpy(productions[1].right, "+TX");

    // X -> @ (epsilon)
    productions[2].left = 'X';
    strcpy(productions[2].right, "@");

    // T -> FY
    productions[3].left = 'T';
    strcpy(productions[3].right, "FY");

    // Y -> *FY
    productions[4].left = 'Y';
    strcpy(productions[4].right, "*FY");

    // Y -> @ (epsilon)
    productions[5].left = 'Y';
    strcpy(productions[5].right, "@");

    // F -> (E)
    productions[6].left = 'F';
    strcpy(productions[6].right, "(E)");

    // F -> i
    productions[7].left = 'F';
    strcpy(productions[7].right, "i");

    // Print the grammar
    printf("Grammar:\n");
    for (int i = 0; i < num_productions; i++) {
        printf("%c -> %s\n", productions[i].left, productions[i].right);
    }

    // Compute FIRST and FOLLOW sets
    compute_first_sets();
    compute_follow_sets();

    // Print FIRST sets
    printf("\nFIRST sets:\n");
    for (int i = 0; i < 26; i++) {
        if (strlen(first[i]) > 0) {
            printf("FIRST(%c) = { ", i + 'A');
            for (int j = 0; j < strlen(first[i]); j++) {
                printf("%c ", first[i][j]);
            }
            printf("}\n");
        }
    }

    // Print FOLLOW sets
    printf("\nFOLLOW sets:\n");
    for (int i = 0; i < 26; i++) {
        if (strlen(follow[i]) > 0) {
            printf("FOLLOW(%c) = { ", i + 'A');
            for (int j = 0; j < strlen(follow[i]); j++) {
                printf("%c ", follow[i][j]);
            }
            printf("}\n");
        }
    }

    return 0;
}
