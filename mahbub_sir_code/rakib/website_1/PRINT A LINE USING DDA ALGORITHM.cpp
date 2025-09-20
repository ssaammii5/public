

#include <graphics.h>

#include <conio.h>

#include <stdio.h>

#include <dos.h>

void main()

{
    int x1, x2, y1, y2, dx, dy, m, x, y;

    int gd = DETECT, gm;

    initgraph(&gd, &gm, "D:\tc\bgi");

    printf("Enter the value of points = ");

    scanf("%d%d%d%d", &x1, &x2, &y1, &y2);

    dx = x2 - x1;

    dy = y2 - y1;

    m = dy / dx;

    x = x1;

    y = y1;

    putpixel(x, y, WHITE);

    if (m < 1)

        while (x < x2)

        {

            x = x + 1;

            y = y + 1;

            putpixel(x, y, WHITE);
        }

    else

        while (y <= y2)

        {

            y = y + 1;

            x = x + 1 / m;

            putpixel(x, y, WHITE);
        }

    getch();

    closegraph();
}
