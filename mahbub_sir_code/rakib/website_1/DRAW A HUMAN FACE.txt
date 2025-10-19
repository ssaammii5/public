#include <graphics.h>

#include <conio.h>

int main()

{

    int gd = DETECT, gm;

    initgraph(&gd, &gm, "D:\TC\BGI");

    circle(300, 180, 80);

    circle(270, 150, 10);

    circle(320, 150, 10);

    line(300, 170, 300, 200);

    arc(300, 180, 240, 300, 50);

    outtextxy(280, 280, "HUMAN FACE");

    getch();

    closegraph();
}
