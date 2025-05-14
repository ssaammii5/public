#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Define structure for syntax tree node
struct TreeNode {
    char data;
    struct TreeNode *left;
    struct TreeNode *right;
};

// Function to create a new node
struct TreeNode* createNode(char data) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to build syntax tree using functions similar to those described in tutorials
struct TreeNode* mknode(char op, struct TreeNode* left, struct TreeNode* right) {
    struct TreeNode* node = createNode(op);
    node->left = left;
    node->right = right;
    return node;
}

struct TreeNode* mkleaf(char id) {
    return createNode(id);
}

// Simple recursive descent parser for expressions
// This is a simplified version and doesn't handle all cases
int pos = 0;
char* expr;

struct TreeNode* parseExpression();
struct TreeNode* parseTerm();
struct TreeNode* parseFactor();

struct TreeNode* parseExpression() {
    struct TreeNode* left = parseTerm();

    while (expr[pos] == '+' || expr[pos] == '-') {
        char op = expr[pos++];
        struct TreeNode* right = parseTerm();
        left = mknode(op, left, right);
    }

    return left;
}

struct TreeNode* parseTerm() {
    struct TreeNode* left = parseFactor();

    while (expr[pos] == '*' || expr[pos] == '/') {
        char op = expr[pos++];
        struct TreeNode* right = parseFactor();
        left = mknode(op, left, right);
    }

    return left;
}

struct TreeNode* parseFactor() {
    if (expr[pos] == '(') {
        pos++; // Skip '('
        struct TreeNode* node = parseExpression();
        pos++; // Skip ')'
        return node;
    } else if (isalnum(expr[pos])) {
        return mkleaf(expr[pos++]);
    }

    // Error handling would go here in a real implementation
    return NULL;
}

// Helper function to get the height of the tree
int getHeight(struct TreeNode* root) {
    if (root == NULL)
        return 0;

    int leftHeight = getHeight(root->left);
    int rightHeight = getHeight(root->right);

    return (leftHeight > rightHeight) ? leftHeight + 1 : rightHeight + 1;
}

// Function to print the tree level by level with fixed spacing
void printLevel(struct TreeNode* root, int level, int space, int width) {
    if (root == NULL)
        return;

    if (level == 1) {
        // Print spaces before the node
        for (int i = 0; i < space; i++)
            printf(" ");
        printf("%c", root->data);
    }
    else if (level > 1) {
        // Use width to determine spacing
        int offset = width / (1 << level);
        printLevel(root->left, level - 1, space - offset, width);
        printLevel(root->right, level - 1, space + offset, width);
    }
}

// Function to print branches between levels with fixed spacing
void printBranches(struct TreeNode* root, int level, int space, int width) {
    if (root == NULL || level == 1)
        return;

    if (level > 1) {
        // Use width to determine spacing
        int offset = width / (1 << level);
        printBranches(root->left, level - 1, space - offset, width);

        // Print spaces before the branch
        for (int i = 0; i < space - 1; i++)
            printf(" ");

        if (root->left && level - 1 == 1)
            printf("/");

        // Print spaces between branches
        int branchSpace = 2 * offset - 1;
        for (int i = 0; i < branchSpace; i++)
            printf(" ");

        if (root->right && level - 1 == 1)
            printf("\\");

        printBranches(root->right, level - 1, space + offset, width);
    }
}

// Function to print the tree in a visual format with fixed spacing
void printTree(struct TreeNode* root) {
    int h = getHeight(root);
    // Use a fixed width based on the tree height
    int width = 4 * (1 << (h - 1));
    int space = width / 2;

    for (int i = 1; i <= h; i++) {
        printLevel(root, i, space, width);
        printf("\n");
        if (i < h) {
            printBranches(root, i + 1, space, width);
            printf("\n");
        }
    }
}

// Function to free the memory allocated for the tree
void freeTree(struct TreeNode* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

int main() {
    char expression[100];

    printf("Enter an expression (e.g., a+b*c): ");
    scanf("%s", expression);

    expr = expression;
    pos = 0;
    struct TreeNode* root = parseExpression();

    if (root == NULL) {
        printf("Invalid expression format\n");
        return 1;
    }

    printf("\nSyntax Tree structure:\n");
    printTree(root);

    // Free allocated memory
    freeTree(root);

    return 0;
}
