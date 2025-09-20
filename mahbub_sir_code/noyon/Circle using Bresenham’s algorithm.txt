#include <graphics.h>

void drawCircle(int xc, int yc, int x, int y)
{
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);
    putpixel(xc + y, yc + x, WHITE);
    putpixel(xc - y, yc + x, WHITE);
    putpixel(xc + y, yc - x, WHITE);
    putpixel(xc - y, yc - x, WHITE);
    delay(10);
}

void BresenhamCircle(int xc, int yc, int r)
{
    int x = 0, y = r;
    int p = 3 - 2 * r;

    drawCircle(xc, yc, x, y);

    while (y >= x)
    {
        x++;

        if (p < 0)
        {
            p = p + 4 * x + 6;
        }
        else
        {
            y--;
            p = p + 4 * (x - y) + 10;
        }

        drawCircle(xc, yc, x, y);
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int xc = 300, yc = 300, r = 100;
    BresenhamCircle(xc, yc, r);

    getch();
    closegraph();
    return 0;
}

