#include <iostream>
#include <graphics.h>
using namespace std;

void Bresenham(int x0, int y0, int x1, int y1)
{
    int dx, dy, p, x, y;

    dx = x1 - x0;
    dy = y1 - y0;
    x = x0;
    y = y0;

    p = 2 * dy - dx;

    while (x <= x1)
    {
        putpixel(x, y, WHITE);
        delay(10);

        if (p >= 0)
        {
            y = y + 1;
            p = p + 2 * dy - 2 * dx;
        }
        else
        {
            p = p + 2 * dy;
        }

        x = x + 1;
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int x1, y1, x2, y2;
    cout << "Enter the coordinates of the starting point (x1, y1): ";
    cin >> x1 >> y1;
    cout << "Enter the coordinates of the ending point (x2, y2): ";
    cin >> x2 >> y2;

    Bresenham(x1, y1, x2, y2);


    getch();
    closegraph();
    return 0;
}
