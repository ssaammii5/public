#include <graphics.h>

#include <conio.h>

char line_styles[] = {SOLID_LINE, DOTTED_LINE, CENTER_LINE, DASHED_LINE, USERBIT_LINE};

void main()

{

    int gd = DETECT, gm, c, x = 100, y = 50;

    initgraph(&gd, &gm, "D:\TC\BGI");

    for (c = 0; c < 5; c++)

    {

        setlinestyle(c, 0, 2);

        line(x, y, x + 200, y);

        y = y + 25;
    }

    getch();

    closegraph();
}