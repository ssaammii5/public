// Lab 05 - Recognize blank, white space, tab, and newline

#include <stdio.h>
#include <ctype.h>

int main() {
    int blank_count = 0;       // Only space characters
    int tab_count = 0;         // Only tab characters
    int newline_count = 0;     // Only newline characters
    int whitespace_count = 0;  // All whitespace characters
    int c;

    printf("Enter text (type 'zz' on a new line to end):\n");

    char prev = '\0';
    while(1) {
        c = getchar();

        // Check for 'zz' sequence on a new line
        if(prev == 'z' && c == 'z') {
            break;
        }

        if(isspace(c))
            whitespace_count++;

        if(c == ' ')
            blank_count++;
        else if(c == '\t')
            tab_count++;
        else if(c == '\n')
            newline_count++;

        prev = c;
    }

    printf("\nCounts:\n");
    printf("Blanks (spaces): %d\n", blank_count);
    printf("Tabs: %d\n", tab_count);
    printf("Newlines: %d\n", newline_count);
    printf("All whitespace characters: %d\n", whitespace_count);

    return 0;
}
