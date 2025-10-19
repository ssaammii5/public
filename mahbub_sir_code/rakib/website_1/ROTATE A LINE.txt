

#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <math.h>

int main()

{

    int gd = DETECT, gm;

    int h, k, x, y, x1, x2, y1, y2, x3, y3, x11, y11, x21, y21, x31, y31;

    float theta, t;

    initgraph(&gd, &gm, "D:\tc\bgi");

    x1 = 100;

    y1 = 100;

    x2 = 150;

    y2 = 150;

    x3 = 200;

    y3 = 150;

    theta = 30;

    setcolor(3);

    line(x1, y1, x2, y2);

    line(x2, y2, x3, y3);

    line(x1, y1, x3, y3);

    getch();

    t = theta * 3.14 / 180;

    x11 = x1 * cos(t) - y1 * sin(t);

    y11 = x1 * sin(t) + y1 * cos(t);

    x21 = x2 * cos(t) - y2 * sin(t);

    y21 = x2 * sin(t) + y2 * cos(t);

    x31 = x3 * cos(t) - y3 * sin(t);

    y31 = x3 * sin(t) + y3 * cos(t);

    setcolor(6);

    line(x11, y11, x21, y21);

    line(x21, y21, x31, y31);

    line(x31, y31, x11, y11);

    getch();

    closegraph();
}
