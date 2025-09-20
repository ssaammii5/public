#include <graphics.h>
#include <conio.h>
#include <dos.h>
#include <stdlib.h>
#include <math.h>
#include <time.h> // Include for seeding rand()

int main()
{
    int gd = DETECT, gm;
    int x, y;

    // Seed the random number generator
    srand(time(0));

    initgraph(&gd, &gm, "D:\\TC\\BGI");

    x = getmaxx() / 2;
    y = getmaxy() / 2;

    while (!kbhit())
    {
        setcolor(rand() % getmaxcolor());
        circle(rand() % x, rand() % y, rand() % 400);
        delay(1000);
    }

    getch();
    closegraph();
}
