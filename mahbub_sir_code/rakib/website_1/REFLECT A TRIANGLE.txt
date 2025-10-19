

#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <stdlib.h>

int main()

{

    int gd = DETECT, gm;

    int m, x1, x2, y1, y2, x3, y3, xx1, xx2, xx3, yy1, yy2, yy3;

    int x11, x22, x33, y11, y22, y33, xmax, ymax, i, a = 0, x12, x13, x14, y12, y13, y14;

    initgraph(&gd, &gm, "c:\tc\bgi");

    xmax = 320;

    ymax = 240;

    line(320, 0, 320, 470);

    line(0, 240, 670, 240);

    outtextxy(325, 245, "(0,0)");

    outtextxy(5, 245, "X");

    outtextxy(620, 245, "X");

    outtextxy(320, 5, "Y");

    outtextxy(320, 450, "Y");

    printf("enter the value of x1=");

    scanf("%d", &xx1);

    printf("enter the value of y1=");

    scanf("%d", &yy1);

    printf("enter the value of x2=");

    scanf("%d", &xx2);

    printf("enter the value of y2=");

    scanf("%d", &yy2);

    printf("enter the value of x3=");

    scanf("%d", &xx3);

    printf("enter the value of y3=");

    scanf("%d", &yy3);

    x1 = xx1 + xmax;

    x2 = xx2 + xmax;

    x3 = xx3 + xmax;

    y1 = ymax - yy1;

    y2 = ymax - yy2;

    y3 = ymax - yy3;

    line(x1, y1, x2, y2);

    line(x2, y2, x3, y3);

    line(x3, y3, x1, y1);

    getch();

    x12 = xmax - xx1;

    x13 = xmax - xx2;

    x14 = xmax - xx3;

    y12 = ymax - yy1;

    y13 = ymax - yy2;

    y14 = ymax - yy3;

    line(x12, y12, x13, y13);

    line(x13, y13, x14, y14);

    line(x12, y12, x14, y14);

    getch();

    x12 = xmax + xx1;

    x13 = xmax + xx2;

    x14 = xmax + xx3;

    y12 = ymax + yy1;

    y13 = ymax + yy2;

    y14 = ymax + yy3;

    line(x12, y12, x13, y13);

    line(x13, y13, x14, y14);

    line(x12, y12, x14, y14);

    getch();

    closegraph();
}
