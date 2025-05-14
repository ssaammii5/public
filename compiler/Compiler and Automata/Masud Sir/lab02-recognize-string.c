// lab 02 - Recognize String Under 'a', 'a*b+', 'abb'

#include <stdio.h>
#include <string.h>

int match_a(char* str) {
    return (str[0] == 'a' && str[1] == '\0');
}

int match_astar_bplus(char* str) {
    int i = 0;
    // Check for 'a's
    while(str[i] == 'a') {
        i++;
    }
    // Must have at least one 'b'
    if(str[i] != 'b') return 0;

    // Check remaining characters are all 'b's
    while(str[i] == 'b') {
        i++;
    }

    // If we reached the end, it's a match
    return (str[i] == '\0');
}

int match_abb(char* str) {
    return (str[0] == 'a' && str[1] == 'b' && str[2] == 'b' && str[3] == '\0');
}

void main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);

    if(match_a(str))
        printf("String matches pattern 'a'\n");
    else if(match_abb(str))  // Check for specific pattern first
        printf("String matches pattern 'abb'\n");
    else if(match_astar_bplus(str))
        printf("String matches pattern 'a*b+'\n");
    else
        printf("String doesn't match any pattern\n");
}
