#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
void disp();
float x,y;
int xc,yc;
int main()
{
                int gd=DETECT,gm,a,b;
                float p1,p2;

                initgraph(&gd,&gm,"c:\\turboc3\\bgi");
                printf("*** Ellipse Generating Algorithm ***\n");
                printf("Enter the value of Xc\t");
                scanf("%d",&xc);
                printf("Enter the value of yc\t");
                scanf("%d",&yc);
                printf("Enter X axis length\t");
                scanf("%d",&a);
                printf("Enter Y axis length\t");
                scanf("%d",&b);
                x=0;y=b;
                disp();
                p1=(b*b)-(a*a*b)+(a*a)/4;
                while((2.0*b*b*x)<=(2.0*a*a*y))
                {
                                x++;
                                if(p1<=0)
                                p1=p1+(2.0*b*b*x)+(b*b);
                                else
        {
                                                y--;
                                                p1=p1+(2.0*b*b*x)+(b*b)-(2.0*a*a*y);
         }
                               disp();
                               x=-x;
                               disp();
                               x=-x;
                               delay(50);
                 }
                 x=a;
                 y=0;
                 disp();
                 p2=(a*a)+2.0*(b*b*a)+(b*b)/4;
                 while((2.0*b*b*x)>(2.0*a*a*y))
                {
                                y++;
                                if(p2>0)
                                p2=p2+(a*a)-(2.0*a*a*y);
                                else
        {
                                                x--;
                                                p2=p2+(2.0*b*b*x)-(2.0*a*a*y)+(a*a);
         }
                                disp();
                                y=-y;
                                disp();
                                y=-y;
                                delay(50);
            }
                getch();
                closegraph();
}
 void disp()
{
              putpixel(xc+x,yc+y,7);
               putpixel(xc-x,yc+y,7);
               putpixel(xc+x,yc-y,7);
          putpixel(xc+x,yc-y,7);
  }
