

#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

void main()

{

    int gd = DETECT, gm;

    float x, y, y1, y2, x1, x2, p, dx, dy;

    initgraph(&gd, &gm, "D:\tc\bgi");

    printf("Enter the values=");

    scanf("%f%f%f%f", &x1, &x2, &y1, &y2);

    dx = x2 - x1;

    dy = y2 - y1;

    p = 2 * dy - dx;

    x = x1;

    y = y1;

    putpixel(x, y, WHITE);

    while (x < x2)

    {

        if (p < 0)

        {

            p = p + 2 * dy;
        }

        else

        {

            p = p + 2 * dy - 2 * dx;

            y++;
        }

        x++;

        putpixel(x, y, 15);
    }

    getch();

    closegraph();
}
