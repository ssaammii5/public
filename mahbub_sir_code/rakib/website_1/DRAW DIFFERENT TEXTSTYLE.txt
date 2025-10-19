#include <graphics.h>

#include <conio.h>

char font_names[] = {DEFAULT_FONT, TRIPLEX_FONT, SMALL_FONT, SANS_SERIF_FONT, GOTHIC_FONT, SCRIPT_FONT, SIMPLEX_FONT, TRIPLEX_SCR_FONT, COMPLEX_FONT, EUROPEAN_FONT, BOLD_FONT};

int main()

{

    int gd = DETECT, gm, x = 25, y = 25, font = 0;

    initgraph(&gd, &gm, "D:\TC\BGI");

    for (font = 0; font <= 10; font++)

    {

        settextstyle(font, HORIZ_DIR, 1);

        outtextxy(x, y, "Text with different fonts");

        y = y + 25;
    }

    getch();

    closegraph();
}
