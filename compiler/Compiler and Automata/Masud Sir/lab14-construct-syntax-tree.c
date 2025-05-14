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

// Function to print the tree in a more structured format
void printTree(struct TreeNode* root) {
    if (root == NULL) return;

    int height = getHeight(root);
    int width = (1 << height) * 2;
    char** grid = (char**)malloc(height * 2 * sizeof(char*));

    for (int i = 0; i < height * 2; i++) {
        grid[i] = (char*)malloc(width * sizeof(char));
        memset(grid[i], ' ', width);
        grid[i][width-1] = '\0';
    }

    // Fill the grid with the tree structure
    void fillGrid(struct TreeNode* node, int row, int col, int height) {
        if (node == NULL) return;

        // Place the node value
        grid[row][col] = node->data;

        // If left child exists
        if (node->left) {
            grid[row+1][col-1] = '/';
            fillGrid(node->left, row+2, col-2, height);
        }

        // If right child exists
        if (node->right) {
            grid[row+1][col+1] = '\\';
            fillGrid(node->right, row+2, col+2, height);
        }
    }

    fillGrid(root, 0, width/2, height);

    // Print the grid
    for (int i = 0; i < height * 2; i++) {
        // Skip empty lines
        int isEmpty = 1;
        for (int j = 0; j < width-1; j++) {
            if (grid[i][j] != ' ') {
                isEmpty = 0;
                break;
            }
        }
        if (!isEmpty) {
            printf("%s\n", grid[i]);
        }
    }

    // Free the grid memory
    for (int i = 0; i < height * 2; i++) {
        free(grid[i]);
    }
    free(grid);
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
