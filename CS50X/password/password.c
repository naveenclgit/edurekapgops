// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int namlen = strlen(password);
    string fname = password;
    int upc = 0;
    int loc = 0;
    int num = 0;
    int sym = 0;

    for (int i = 0; i < namlen; i++)
    {
        //doing it with if condition
        if (isupper(fname[i]))
        {
            upc = 1;
        }
        else if (islower(fname[i]))
        {
            loc = 1;
        }
        else if (isdigit(fname[i]))
        {
            num = 1;
        }
        else if (ispunct(fname[i]))
        {
            sym = 1;
        }
    }
    // if all is well then retrun true
    if (upc == 1 && loc == 1 && num == 1 && sym == 1)
    {
        return true;
    }

    return false;
}
