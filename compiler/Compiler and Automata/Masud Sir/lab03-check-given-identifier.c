// Lab 03 - Test whether a given identifier is valid or not

#include <stdio.h>
#include <ctype.h>
#include <string.h>

int is_valid_identifier(char* id) {
    // Check if first character is a letter or underscore
    if(!(isalpha(id[0]) || id[0] == '_'))
        return 0;

    // Check remaining characters
    for(int i = 1; i < strlen(id); i++) {
        if(!(isalnum(id[i]) || id[i] == '_'))
            return 0;
    }

    return 1;
}

void main() {
    char identifier[100];

    printf("Enter an identifier: ");
    scanf("%s", identifier);

    if(is_valid_identifier(identifier))
        printf("%s is a valid identifier\n", identifier);
    else
        printf("%s is not a valid identifier\n", identifier);
}
