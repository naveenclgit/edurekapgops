#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int getcardnumcheck(const char *cnumber);
string getcardtype(const char *cnumber);
int iscardvalid(const char *cnumber);

int main(void)
{
    string vald = "INVALID";
    string cnumber;
    do
    {
        // Get card number and basic validation
        cnumber = get_string("Number: ");
    }
    while (getcardnumcheck(cnumber) != 1 && getcardnumcheck(cnumber) != 2);

    // Validate card number
    if (getcardnumcheck(cnumber) == 1)
    {
        vald = "VALID";
        //printf("%s\n",vald);
    }
    else if (getcardnumcheck(cnumber) == 2)
    {
        printf("%s\n", vald);
    }

    // printf("%s\n",vald);
    // if card is valid proceed to procees other checks
    if (strcmp(vald, "VALID") == 0)
    {
        int crdvld = iscardvalid(cnumber);
        if (crdvld == 1)
        {
            //printf(" VALID\n");
            string crdtype = getcardtype(cnumber);
            printf("%s\n", crdtype);
        }
        else
        {
            printf("INVALID\n");
        }
    }

}


// Function to check the card number format validity

int getcardnumcheck(const char *cnumber)
{
    int cnleng = strlen(cnumber);
    int a, b;
    // checking if card number has invalid chars
    for (int i = 0; i < cnleng; i++)
    {
        if (cnumber[i] < '0' || cnumber[i] > '9')
        {
            a = 0;
            return 0;
        }
        else
        {
            a = 1;
        }
    }

    // checking card number length
    if (cnleng != 13 && cnleng != 15 && cnleng != 16)
    {
        b = 0;
    }
    else if (cnleng == 13 || cnleng == 15 || cnleng == 16)
    {
        b = 1;
    }

    //matching both conditions
    if (a == 0)
    {
        return 0;
    }
    else if (a == 1 && b == 1)
    {
        return 1;
    }
    else if (a == 1 && b == 0)
    {
        return 2;
    }

    return 0;
}


// Function to get card type.

string getcardtype(const char *cnumber)
{

    string mystring = (string)cnumber;
    char *s = mystring;
    if (s != NULL)
    {
        char *t = malloc(strlen(s) + 1);
        if (t != NULL)
        {
            strcpy(t, s);
            t[2] = '\0';
            //printf("s: %s\n", s);
            //printf("t: %s\n", t);
            //comparing extracted first 2 digits of the card number
            if (strcmp(t, "51") == 0 || strcmp(t, "52") == 0 || strcmp(t, "53") == 0 || strcmp(t, "54") == 0 || strcmp(t, "55") == 0)
            {
                return "MASTERCARD";

            }
            else if (strcmp(t, "34") == 0 || strcmp(t, "37") == 0)
            {
                return "AMEX";

            }
            //if above is not matched then checking first lettter 4 for visa
            strcpy(t, s);
            t[1] = '\0';
            if (strcmp(t, "4") == 0)
            {
                return "VISA";
            }
        }


    }
    return "INVALID";
}



int iscardvalid(const char *cnumber)
{
    int lent = strlen(cnumber);
    int total = 0;
    int second = 0;
    //applying Luhn’s Algorithm
    for (int i = lent - 1; i >= 0; i--)
    {
        int eadg = cnumber[i] - '0';
        if (second)
        {
            eadg *= 2;
            if (eadg > 9)
            {
                eadg = eadg / 10 + eadg % 10;
            }
        }

        total += eadg;
        second = !second;
    }

    return (total % 10 == 0);
}