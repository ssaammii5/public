
#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

void main()

{

    int gd = DETECT, gm;

    int x, y;

    initgraph(&gd, &gm, "D:\TC\BGI");

    x = getmaxx() / 2;

    y = getmaxy() / 2;

    while (!kbhit())

    {

        putpixel(random(600), random(600), random(600));

        circle(random(x), random(y), random(5));

        delay(1000);
    }

    getch();

    closegraph();
}
