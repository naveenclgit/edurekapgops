#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    float result = 0.0;
    char o = output;
    char b = 'A';
    char c = 'T';

    if (o == b)
    {
        // printf("%c\n",output);
        // if output is A find average
        for (int i = 0; i < weeks; i++)
        {
            result += hours[i];
        }
        result = result / weeks;
    }
    else if (o == c)
    {
        // if output is T find total
        // printf("%c\n",output);
        for (int i = 0; i < weeks; i++)
        {
            result += hours[i];
        }

    }
// retrun the result

    return result;

}