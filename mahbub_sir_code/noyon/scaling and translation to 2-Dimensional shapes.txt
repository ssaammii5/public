#include <graphics.h>
#include <stdio.h>

void drawShape(int x[], int y[], int n) {
    for (int i = 0; i < n - 1; i++) {
        line(x[i], y[i], x[i + 1], y[i + 1]);
    }
    line(x[n - 1], y[n - 1], x[0], y[0]);
}

void scaleShape(int x[], int y[], int n, float Sx, float Sy) {
    for (int i = 0; i < n; i++) {
        x[i] = x[i] * Sx;
        y[i] = y[i] * Sy;
    }
}

void shearShape(int x[], int y[], int n, float Shx, float Shy) {
    for (int i = 0; i < n; i++) {
        int newX = x[i] + Shx * y[i];
        int newY = y[i] + Shy * x[i];
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

    float Shx = 0.2, Shy = 0;
    shearShape(x, y, n, Shx, Shy);

    setcolor(GREEN);
    drawShape(x, y, n);

    getch();
    closegraph();
    return 0;
}
