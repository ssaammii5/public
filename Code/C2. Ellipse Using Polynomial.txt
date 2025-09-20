#include <graphics.h>
#include <math.h>

void PolynomialEllipse(int xc, int yc, int rx, int ry)
{
    float theta;
    int x, y;

    for (theta = 0; theta < 2 * M_PI; theta += 0.001)
    {
        x = xc + rx * cos(theta);
        y = yc + ry * sin(theta);

        putpixel(x, y, WHITE);
        delay(0.8);
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int xc = 250, yc = 250;
    int rx = 150, ry = 100;

    PolynomialEllipse(xc, yc, rx, ry);

    getch();
    closegraph();
    return 0;
}
