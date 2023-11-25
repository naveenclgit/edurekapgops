cd #include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startnum = 0;

    do
    {
        startnum = get_int("Start size: ");
    }
    while (startnum < 9);

    // TODO: Prompt for end size
    int endnum = 0;

    do
    {
        endnum = get_int("End Size: ");
    }
    while (endnum<startnum);

    // TODO: Calculate number of years until we reach threshold
    int tgteyar = 0;
    while (startnum<endnum)
    {
        startnum = (startnum + (startnum / 3)) - (startnum / 4);
        // printf("End Size: %i\n",startnum);
        tgteyar ++;
    }

    // TODO: Print number of years
    printf ("Years: %i \n",tgteyar);
}
