#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string mymessage = get_string("Message: ");
    int msglen = strlen(mymessage);
    int decml = 0 ;

    for (int i = 0 ; i < msglen; i++)
    {
        decml = mymessage[i];
        // printf("Decm %i\n",decml);


        if (decml == 0)
        {
            return 0;
        }

        int binary[] = {0, 0, 0, 0, 0, 0, 0, 0} ;
        int n = 0;

        while (decml > 0)
        {
            binary[n] = decml % 2;
            decml /= 2 ;
            n++;
        }

        for (int j = 7; j >= 0 ; j--)
        {
            // printf ("%i", binary[j]);
            print_bulb(binary[j]);


        }
        printf("\n");
    }
}


void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}


