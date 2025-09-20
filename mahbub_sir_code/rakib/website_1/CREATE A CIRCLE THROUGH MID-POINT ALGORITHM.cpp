
#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

int main()

{

    int x, y, h, k, r, p;

    int gd = DETECT, gm;

    initgraph(&gd, &gm, "D:\tc\bgi");

    printf(" Enter the center=");

    scanf("%d%d", &h, &k);

    printf("Enter the radius=");

    scanf("%d", &r);

    x = 0;

    y = r;

    p = 1 - r;

    while (x < y)

    {

        if (p < 0)

        {

            p = p + (2 * x) + 3;
        }

        else

        {

            p = p + 2 * (x - y) + 5;

            y = y - 1;
        }

        x++;

        putpixel(x + h, y + k, 15);

        putpixel(y + h, x + k, 15);

        putpixel(-x + h, -y + k, 15);

        putpixel(-y + h, -x + k, 15);

        putpixel(-x + h, y + k, 15);

        putpixel(x + h, -y + k, 15);

        putpixel(y + h, -x + k, 15);

        putpixel(-y + h, x + k, 15);
    }

    getch();

    closegraph();
}
