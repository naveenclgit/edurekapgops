#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input, int len);

int num = 0;

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("Intiget is %i\n", convert(input, strlen(input) - 1));

    int mynum = convert(input, strlen(input) - 1);
    printf("Sumacumlaude is  %i\n", mynum + 4);
}



int convert(string input, int len)
{
    // TODO

    //if (len < 0 || (input[len] < '0' || input[len] > '9'))
    if (len < 0)

    {
        return 0;
    }

    //printf("%c\n", input[len]);
    // printf("%i , %c \n", len, input[len - 1]);
    return (10 * convert(input, len - 1) + (input[len] - '0'));

}



