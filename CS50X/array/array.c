#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int len;
    do
    {
        len = get_int("Length :");
    }
    while (len < 1 );

    int tw[len];
    tw[0]=1;

    printf("%i\n",tw[0] );
    for (int i =1 ; i < len; i++ )
    {
        tw[i]= tw[i-1] * 2 ;
        printf("%i\n",tw[i]);
    }
}