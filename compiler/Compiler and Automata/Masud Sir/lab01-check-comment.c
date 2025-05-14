// lab 01 - identify whether a given line is a comment or not

#include <stdio.h>
#include <string.h>

void main() {
    char line[100];
    int i = 0;

    printf("Enter a line: ");
    gets(line);

    if(line[0] == '/') {
        if(line[1] == '/') {
            printf("It is a single-line comment");
        }
        else if(line[1] == '*') {
            for(i = 2; i < strlen(line) - 1; i++) {
                if(line[i] == '*' && line[i+1] == '/') {
                    printf("It is a multi-line comment");
                    break;
                }
            }
            if(i == strlen(line) - 1)
                printf("It is not a comment");
        }
        else {
            printf("It is not a comment");
        }
    }
    else {
        printf("It is not a comment");
    }
}
