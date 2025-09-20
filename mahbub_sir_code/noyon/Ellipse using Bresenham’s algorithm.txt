#include <graphics.h>

void drawEllipse(int xc, int yc, int x, int y)
{
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);
    delay(10);
}

void BresenhamEllipse(int xc, int yc, int rx, int ry)
{
    int x = 0;
    int y = ry;

    int rx2 = rx * rx;
    int ry2 = ry * ry;
    int tworx2 = 2 * rx2;
    int twory2 = 2 * ry2;
    int p1 = ry2 - (rx2 * ry) + (0.25 * rx2);

    int px = 0;
    int py = tworx2 * y;

    while (px < py)
    {
        drawEllipse(xc, yc, x, y);

        x++;
        px += twory2;

        if (p1 < 0)
        {
            p1 += ry2 + px;
        }
        else
        {
            y--;
            py -= tworx2;
            p1 += ry2 + px - py;
        }
    }

    int p2 = (ry2) * (x + 0.5) * (x + 0.5) + (rx2) * (y - 1) * (y - 1) - (rx2 * ry2);

    while (y >= 0)
    {
        drawEllipse(xc, yc, x, y);

        y--;
        py -= tworx2;

        if (p2 > 0)
        {
            p2 += rx2 - py;
        }
        else
        {
            x++;
            px += twory2;
            p2 += rx2 - py + px;
        }
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int xc = 250, yc = 250, rx = 150, ry = 100;
    BresenhamEllipse(xc, yc, rx, ry);

    getch();
    closegraph();
    return 0;
}
