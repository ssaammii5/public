#include <graphics.h>
#include <math.h>
#include <stdio.h>

void drawShape(int x[], int y[], int n) {
    for (int i = 0; i < n - 1; i++) {
        line(x[i], y[i], x[i + 1], y[i + 1]);
    }
    line(x[n - 1], y[n - 1], x[0], y[0]);

    delay(1000);
}

void scaleShape(int x[], int y[], int n, float Sx, float Sy) {
    for (int i = 0; i < n; i++) {
        x[i] = x[i] * Sx;
        y[i] = y[i] * Sy;
    }
}

void rotateShape(int x[], int y[], int n, float angle) {
    float rad = angle * M_PI / 180; // Convert angle to radians
    for (int i = 0; i < n; i++) {
        int newX = x[i] * cos(rad) - y[i] * sin(rad);
        int newY = x[i] * sin(rad) + y[i] * cos(rad);
        x[i] = newX;
        y[i] = newY;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int x[] = {100, 200, 150};
    int y[] = {100, 100, 200};
    int n = 3;

    setcolor(WHITE);
    drawShape(x, y, n);

    float Sx = 1.5, Sy = 1.5;
    scaleShape(x, y, n, Sx, Sy);

    setcolor(RED);
    drawShape(x, y, n);

    float angle = 30;
    rotateShape(x, y, n, angle);

    setcolor(GREEN);
    drawShape(x, y, n);

    getch();
    closegraph();
    return 0;
}
