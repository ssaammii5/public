// Lab 09 - constructing recursive descent parsing

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char input[100];
int pos = 0;
char lookahead;

void error() {
    printf("\nSyntax Error!\n");
    exit(1);
}

void match(char c) {
    if(lookahead == c)
        lookahead = input[++pos];
    else
        error();
}

// Forward declarations
void E();
void Eprime();
void T();
void Tprime();
void F();

// E -> TE'
void E() {
    T();
    Eprime();
}

// E' -> +TE' | ε
void Eprime() {
    if(lookahead == '+') {
        match('+');
        T();
        Eprime();
    }
    // ε production, do nothing
}

// T -> FT'
void T() {
    F();
    Tprime();
}

// T' -> *FT' | ε
void Tprime() {
    if(lookahead == '*') {
        match('*');
        F();
        Tprime();
    }
    // ε production, do nothing
}

// F -> (E) | id
void F() {
    if(lookahead == '(') {
        match('(');
        E();
        match(')');
    }
    else if(lookahead == 'i') {  // id is represented by 'i'
        match('i');
    }
    else {
        error();
    }
}

void main() {
    printf("Enter input string ending with $ (use 'i' for id): ");
    scanf("%s", input);

    lookahead = input[0];

    E();

    if(lookahead == '$')
        printf("\nParsing Successful!\n");
    else
        error();
}
