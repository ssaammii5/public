
#include <stdio.h>

#include <graphics.h>

#include <conio.h>

#include <dos.h>

#include <stdlib.h>

#include <math.h>
int main()

{

    int ch;

    int gd = DETECT, gm;

    void translate();

    void scale();

    void rotate();

    initgraph(&gd, &gm, "D:\tc\bgi");

    printf("1)Translate 2)Scale 3) Rotate");

    printf(" Enter a choice=");

    scanf("%d", &ch);

    switch (ch)

    {

    case 1:
        translate();

        break;

    case 2:
        scale();

        break;

    case 3:
        rotate();

        break;

    default:
        printf("you have entered wrong choice");
        break;
    }

    getch();

    closegraph();
}

void translate()

{

    int tx, ty;

    setcolor(15);

    outtextxy(240, 50, "TRANSLATION");

    outtextxy(238, 60, "------------");

    printf(" Enter tx: ");

    scanf("%d", &tx);

    printf(" Enter ty: ");

    scanf("%d", &ty);

    rectangle(200, 150, 150, 200);

    printf(" After Translation");

    rectangle(200 + tx, 150 + ty, 150 + tx, 200 + ty);
}

void scale()

{

    int sx, sy;

    setcolor(15);

    outtextxy(240, 50, "SCALING");

    outtextxy(238, 60, "--------");

    printf(" Enter sx: ");

    scanf("%d", &sx);

    printf(" Enter sy: ");

    scanf("%d", &sy);

    rectangle(200, 150, 150, 200);

    printf(" After Scaling");

    rectangle(200 + sx, 150 + sy, 50 * sx, 200 + sy);
}

void rotate()

{

    float theta;

    int x1, x2, x3, x4, y1, y2, y3, y4;

    int ax1, ax2, ax3, ax4, ay1, ay2, ay3, ay4;

    int refx, refy;

    printf("Enter the angle of rotation=");

    scanf("%f", theta);

    theta = theta * (3.14 / 180);

    setcolor(15);

    outtextxy(240, 80, "ROTATE");

    outtextxy(238, 90, "-------");

    refx = 100;

    refx = 100;

    x1 = 100;

    y1 = 100;

    x2 = 150;

    y2 = 100;

    x3 = 150;

    y3 = 150;

    x4 = 100;

    y4 = 150;

    ax1 = refy + (x1 - refx) * cos(theta) - (y1 - refy) * sin(theta);

    ay1 = refy + (x1 - refx) * sin(theta) + (y1 - refy) * cos(theta);

    ax2 = refy + (x2 - refx) * cos(theta) - (y2 - refy) * sin(theta);

    ay2 = refy + (x2 - refx) * sin(theta) + (y2 - refy) * cos(theta);

    ax3 = refy + (x3 - refx) * cos(theta) - (y3 - refy) * sin(theta);

    ay3 = refy + (x3 - refx) * sin(theta) + (y3 - refy) * cos(theta);

    ax4 = refy + (x4 - refx) * cos(theta) - (y4 - refy) * sin(theta);

    ay4 = refy + (x4 - refx) * sin(theta) + (y4 - refy) * cos(theta);

    rectangle(100, 150, 150, 100);

    line(ax1, ay1, ax2, ay2);

    line(ax2, ay2, ax3, ay3);

    line(ax3, ay3, ax4, ay4);

    line(ax4, ay4, ax1, ay1);
}
