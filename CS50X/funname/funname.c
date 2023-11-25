#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    string fname;
    fname = get_string("What is your name :");
    /* if (argc < 1)
    {
       // fname = get_string("What is your name :");
       printf("I need a Name");
    }
    else
    {
        fname = argv[1];
    }
    */ 
    int namlen = strlen(fname);

    for (int i = namlen; i > -1; i-- )
    {
       // printf ("%i\n",namlen);
       if (i == namlen-1)
       {
            printf ("%c",fname[i]-32);
       }
       else if (i == 0)
       {
            printf ("%c",fname[i]+32);
       }
       else
       {
        printf ("%c",fname[i]);
       }
    }

printf ("\n");
}