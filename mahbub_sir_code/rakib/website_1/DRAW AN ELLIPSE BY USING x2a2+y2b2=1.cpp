#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <math.h>

int main()

{

    int gd = DETECT, gm;

    float x, y;

    int a = 100, b = 80;

    initgraph(&gd, &gm, "D:\tc\bgi");

    do

    {

        x = x + 0.5;

        y = sqrt(b * b * (1 - (x * x) / (a * a)));

        putpixel(320 + x, 240 + y, 15);

        putpixel(320 + x, 240 - y, 15);

        putpixel(320 - x, 240 + y, 15);

        putpixel(320 - x, 240 - y, 15);

    }

    while (x < 99.9);

    getch();
}
