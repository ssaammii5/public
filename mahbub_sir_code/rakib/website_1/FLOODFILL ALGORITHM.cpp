

#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

void floodfil(int x, int y, int fillcolor, int oldcolor);

int main()

{

    int gd = DETECT, gm;

    initgraph(&gd, &gm, "D:\tc\bgi");

    setbkcolor(15);

    setfillstyle(SOLID_FILL, 10);

    bar(50, 50, 100, 100);

    floodfil(70, 70, 12, 10);

    getch();

    closegraph();
}

void floodfil(int x, int y, int fillcolor, int oldcolor)

{

    if (getpixel(x, y) == oldcolor)

    {

        setcolor(fillcolor);

        putpixel(x, y, fillcolor);

        delay(2);

        floodfil(x + 1, y, fillcolor, oldcolor);

        floodfil(x - 1, y, fillcolor, oldcolor);

        floodfil(x, y - 1, fillcolor, oldcolor);

        floodfil(x, y + 1, fillcolor, oldcolor);
    }
}
