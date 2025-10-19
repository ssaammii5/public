
#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

int main()

{

    int i, r1, r2, n, j = 2, xr = 200, yr = 100;

    int gd = DETECT, gm;

    initgraph(&gd, &gm, "D:\tc\bgi");

    printf("enter the no. of Ellipse=");

    scanf("%d", &n);

    r1 = xr / n;

    r2 = yr / n;

    for (i = 0; i < n; i++)

    {

        setfillstyle(1, j);

        ellipse(300, 200, 0, 360, xr, yr);

        if (j == 10)

            j = 2;

        xr = xr - r1;

        yr = yr - r2;

        j++;
    }

    getch();
}
