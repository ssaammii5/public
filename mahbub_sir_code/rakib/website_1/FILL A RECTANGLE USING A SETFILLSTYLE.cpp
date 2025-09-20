#include <graphics.h>
#include <conio.h>
#include <dos.h>

int main()
{
    int midx, midy, style;
    int gd = DETECT, gm;

    // Initialize the graphics mode
    initgraph(&gd, &gm, "D:\\TC\\BGI");

    midx = getmaxx() / 2;
    midy = getmaxy() / 2;

    // Draw a rectangle to display the fill styles
    rectangle(0, 0, midx, midy);

    // Loop through fill styles and display each one
    for (style = 0; style < 12; style++)
    {
        setfillstyle(style, 5); // Set the fill style and color
        rectangle(0, 0, midx, midy); // Draw the rectangle
        floodfill(10, 10, WHITE); // Fill the rectangle

        delay(1000); // Pause to view the fill style
        cleardevice(); // Clear the screen
    }

    getch();
    closegraph(); // Close the graphics mode
}
