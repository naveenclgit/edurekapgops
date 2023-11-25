// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string fname);

int main(int argc, string argv[])
{
    int param = argc;
    // if no value given then print usage 
    if (param < 2 || param > 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }
    string fname = argv[1];
    string output = replace(fname);
    printf("%s\n", output);

}

//Function to replace vowels.

string replace(string fname)
{
    int namlen = strlen(fname);
    char vowels[] = {'a', 'e', 'i', 'o'};
    string printname = fname;

    for (int i = 0; i < namlen; i++)
    {

        //doing it with if condition
        if (fname[i] != vowels[0] && fname[i] != vowels[1] && fname[i] != vowels[2] && fname[i] != vowels[3])
        {
            printname[i] = fname[i];
        }
        else if (fname[i] == vowels[0])
        {
            printname[i] = '6';
        }
        else if (fname[i] == vowels[1])
        {
            printname[i] = '3';
        }
        else if (fname[i] == vowels[2])
        {
            printname[i] = '1';
        }
        else if (fname[i] == vowels[3])
        {
            printname[i] = '0';
        }
    }

    return printname;
}

