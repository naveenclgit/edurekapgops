#include <cs50.h>
#include <stdio.h>


int main(void)
{
    int startnum = 0;
    // Ask for starting number of llamas
    do
    {
        startnum = get_int("How many llamas you have ? ");
    }
    while (startnum < 9);

    int endnum = 0;
    // Ask for target number of llamas
    do
    {
        endnum = get_int("How many llamas you want ? ");
    }
    while (endnum<startnum);

    int tgteyar = 0;
    // How many years it will take to get to target number of llamas
    while (startnum<endnum)
    {
        startnum = (startnum + (startnum / 3)) - (startnum / 4);
        printf("Year %i Now %i \n",tgteyar,startnum);
        tgteyar ++;
    }

    printf ("It will take %i years\n",tgteyar);


}