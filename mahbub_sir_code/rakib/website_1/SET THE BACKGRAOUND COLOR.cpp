#include <graphics.h>

#include <conio.h>

main()

{

    int gd = DETECT, gm, i;

    initgraph(&gd, &gm, "D:\TC\BGI");

    for (i = 0; i < 12; i++)

    {

        setbkcolor(i);

        delay(1000);
    }

    getch();

    closegraph();

    return 0;
}