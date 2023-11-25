#include <cs50.h>
#include <stdio.h>



int main(void)
{
    long x = get_long ("x : " );
    long y = get_long ("y : " );

    printf ("Sum %li\n", x+y );

    float z = (float)x / (float)y;
    printf ("Float %.25f\n", z);

    double a = (double)x / (double)y;
    printf ("Double %.25f\n", a);

}


