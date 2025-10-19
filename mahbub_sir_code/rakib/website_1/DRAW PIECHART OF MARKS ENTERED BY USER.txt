

#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

void main()

{

    int gd = DETECT, gm;

    float x = 0, y = 0, tm, m;

    int c = 1, n = 5;

    initgraph(&gd, &gm, "D:\tc\bgi");

    setbkcolor(WHITE);

    setcolor(BLUE);

    pieslice(300, 250, 0, 360, 100);

    printf("Enter total marks=");

    scanf("%f", &tm);

    while (n > 0)

    {

        printf("Enter marks=");

        scanf("%f", &m);

        setfillstyle(1, c);

        c++;

        y = y + ((m / tm) * 360);

        pieslice(300, 250, x, y, 100);

        x = y;

        n--;
    }

    getch();

    closegraph();
}
