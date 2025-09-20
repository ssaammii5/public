

#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

int main()

{

    int gd = DETECT, gm;

    int xold, xnew, sx, ynew, yold, sy, x1old, y1old, x1new, y1new;

    initgraph(&gd, &gm, "D:\tc\bgi");

    printf("enter the end of the line=");

    scanf("%d %d %d %d ", &xold, &yold, &x1old, y1old);

    line(xold, yold, x1old, y1old);

    printf("enter the translation in x direction and y direction=");

    scanf("%d%d", &sx, &sy);

    xnew = xold + sx;

    ynew = yold + sy;

    x1new = x1old + sx;

    y1new = y1old + sy;

    line(xnew, ynew, x1new, y1new);

    printf(" New coordinates of p1:%d %d", xnew, ynew);

    printf(" New coordinates of p2:%d %d", x1new, y1new);

    getch();

    closegraph();
}
