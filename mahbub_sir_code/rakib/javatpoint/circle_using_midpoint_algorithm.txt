#include <iostream>
#include <graphics.h>
#include <cmath>

using namespace std;

// Function to draw a circle using Midpoint Algorithm
void drawCircle(int xc, int yc, int radius) {
    int x = 0, y = radius;
    int p = 1 - radius;

    // Plot initial point
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);

    while (x <= y) {
        if (p < 0) {
            p = p + 2 * x + 1;
            x++;
        } else {
            p = p + 2 * (x - y) + 1;
            x++;
            y--;
        }

        // Plot points based on the algorithm
        putpixel(xc + x, yc + y, WHITE);
        putpixel(xc - x, yc + y, WHITE);
        putpixel(xc + x, yc - y, WHITE);
        putpixel(xc - x, yc - y, WHITE);
        putpixel(xc + y, yc + x, WHITE);
        putpixel(xc - y, yc + x, WHITE);
        putpixel(xc + y, yc - x, WHITE);
        putpixel(xc - y, yc - x, WHITE);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int xc = 200, yc = 150, radius = 100;

    // Draw the circle
    drawCircle(xc, yc, radius);

    getch();
    closegraph();
    return 0;
}
