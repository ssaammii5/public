

#include <graphics.h>

#include <conio.h>

int main()

{

    int gd = DETECT, gm, midx, midy;

    initgraph(&gd, &gm, "D:\TC\BGI");

    settextstyle(SANS_SERIF_FONT, HORIZ_DIR, 2);

    setcolor(WHITE);

    outtextxy(275, 80, "PIE CHART");

    midx = getmaxx() / 2;

    midy = getmaxy() / 2;

    setfillstyle(LINE_FILL, BLUE);

    pieslice(midx, midy, 0, 75, 100);

    setfillstyle(XHATCH_FILL, RED);

    pieslice(midx, midy, 75, 225, 100);

    setfillstyle(WIDE_DOT_FILL, GREEN);

    pieslice(midx, midy, 225, 360, 100);

    getch();
}
