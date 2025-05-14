// Lab 04 - Recognize tokens from lexemes

#include <stdio.h>
#include <ctype.h>
#include <string.h>

void analyze_token(char* lexeme) {
    // List of C keywords
    char* keywords[] = {"auto", "break", "case", "char", "const", "continue", "default",
                        "do", "double", "else", "enum", "extern", "float", "for", "goto",
                        "if", "int", "long", "register", "return", "short", "signed",
                        "sizeof", "static", "struct", "switch", "typedef", "union",
                        "unsigned", "void", "volatile", "while"};

    int i;
    // Check if lexeme is a keyword
    for(i = 0; i < 32; i++) {
        if(strcmp(lexeme, keywords[i]) == 0) {
            printf("'%s' is a KEYWORD\n", lexeme);
            return;
        }
    }

    // Check if lexeme is an operator
    if(strcmp(lexeme, "+") == 0 || strcmp(lexeme, "-") == 0 || strcmp(lexeme, "*") == 0 ||
       strcmp(lexeme, "/") == 0 || strcmp(lexeme, "%") == 0 || strcmp(lexeme, "=") == 0) {
        printf("'%s' is an OPERATOR\n", lexeme);
        return;
    }

    // Check if lexeme is a valid identifier
    if(isalpha(lexeme[0]) || lexeme[0] == '_') {
        for(i = 1; i < strlen(lexeme); i++) {
            if(!(isalnum(lexeme[i]) || lexeme[i] == '_')) {
                printf("'%s' is an INVALID TOKEN\n", lexeme);
                return;
            }
        }
        printf("'%s' is an IDENTIFIER\n", lexeme);
        return;
    }

    // Check if lexeme is a number
    if(isdigit(lexeme[0])) {
        for(i = 1; i < strlen(lexeme); i++) {
            if(!isdigit(lexeme[i])) {
                printf("'%s' is an INVALID TOKEN\n", lexeme);
                return;
            }
        }
        printf("'%s' is a NUMBER\n", lexeme);
        return;
    }

    // If none of the above
    printf("'%s' is an INVALID TOKEN\n", lexeme);
}

void main() {
    char input[1000], *token;

    printf("Enter input (space-separated lexemes): ");
    gets(input);

    token = strtok(input, " \t\n");
    while(token != NULL) {
        analyze_token(token);
        token = strtok(NULL, " \t\n");
    }
}
