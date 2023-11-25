// Practice working with structs
// Practice applying sorting algorithms

#include <cs50.h>
#include <stdio.h>

#define NUM_CITIES 10

typedef struct
{
    string city;
    int temp;
}
avg_temp;

avg_temp temps[NUM_CITIES];

void sort_citiesas(void);
void sort_citiesds(void);

int main(void)
{
    temps[0].city = "Austin";
    temps[0].temp = 97;

    temps[1].city = "Boston";
    temps[1].temp = 82;

    temps[2].city = "Chicago";
    temps[2].temp = 85;

    temps[3].city = "Denver";
    temps[3].temp = 90;

    temps[4].city = "Las Vegas";
    temps[4].temp = 105;

    temps[5].city = "Los Angeles";
    temps[5].temp = 82;

    temps[6].city = "Miami";
    temps[6].temp = 97;

    temps[7].city = "New York";
    temps[7].temp = 85;

    temps[8].city = "Phoenix";
    temps[8].temp = 107;

    temps[9].city = "San Francisco";
    temps[9].temp = 66;

    // Before sort
    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("BS %s: %i\n", temps[i].city, temps[i].temp);
    }
    // call sort ascending func
    sort_citiesas();

    printf("\nAverage July Temperatures by City\n\n");

    // After Sort
    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("AS %s: %i\n", temps[i].city, temps[i].temp);
    }
    // call sort decending func
    sort_citiesds();

    printf("\nAverage July Temperatures by City\n\n");

    // After Sort
    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("AS %s: %i\n", temps[i].city, temps[i].temp);
    }
}

// TODO: Sort cities by temperature in descending order
void sort_citiesas(void)
{
    // Add your code here for ascending sort - bubble sort
    for (int i = 0 ; i < NUM_CITIES - 1; i++)
    {
        for (int j = 0 ; j < NUM_CITIES - 1; j++)
        {
            if (temps[j].temp > temps[j + 1].temp)
            {
                string tcity = temps[j + 1].city;
                int ttemp = temps[j + 1].temp;
                temps[j + 1].city = temps[j].city;
                temps[j + 1].temp = temps[j].temp;
                temps[j].city = tcity;
                temps[j].temp = ttemp;
            }

        }

    }

}
void sort_citiesds(void)
{
    // Add your code here for decending sort bubble
    for (int i = 0 ; i < NUM_CITIES - 1; i++)
    {
        for (int j = 0 ; j < NUM_CITIES - 1; j++)
        {
            if (temps[j].temp < temps[j + 1].temp)
            {
                string tcity = temps[j].city;
                int ttemp = temps[j].temp;
                temps[j].city = temps[j + 1].city;
                temps[j].temp = temps[j + 1].temp;
                temps[j + 1].city = tcity;
                temps[j + 1].temp = ttemp;
            }

        }

    }

}
