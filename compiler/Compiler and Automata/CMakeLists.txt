cmake_minimum_required(VERSION 3.31)
project(Compiler_and_Automata)

set(CMAKE_CXX_STANDARD 17)

add_executable(Compiler_and_Automata main.cpp
        "Masud Sir/lab01-check-comment.c"
        "Masud Sir/lab02-recognize-string.c"
        "Masud Sir/lab03-check-given-identifier.c"
        "Masud Sir/lab04-recognize-tokens-lexeme.c"
        "Masud Sir/lab05-recognize-blank-space.c"
        "Masud Sir/lab06-simulate-lexical-analyzer.c"
        "Masud Sir/lab07-constructing-ll1-parsing.c"
        "Masud Sir/lab08-implementing-predictive-parser.c"
        "Masud Sir/lab09-constructing-recursive-descent-parsing.c"
        "Masud Sir/lab10-predictive-parser.c"
        "Masud Sir/lab11-calculate-first-and-follow.c"
        "Masud Sir/lab12-top-down-parsing.c"
        "Masud Sir/lab13-bottom-up-parsing.c"
        "Masud Sir/lab14-construct-syntax-tree.c"
        "Masud Sir/lab15-generate-three-address-code.c"
        "Masud Sir/test.c"
        "Masud Sir/test1.c")
