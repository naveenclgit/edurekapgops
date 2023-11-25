#include <cs50.h>
#include <stdio.h>
int get_size(void);
void print_grid(int size);


int main(void)
{
    // Get size for grid
    int n = get_size();

    // Print grid of bricks
    print_grid(n);

    //printf("\n");
}

// Function for getting size

int get_size(void)
{
    // Get size for grid
    int n = 0;
    do
    {
        // get user data
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}


// Function for print grid
void print_grid(int size)
{

    // Print grid, h for hash and s for space
    int h, s;
    for (h = 1; h <= size; h++)
    {

        for (s = 1; s <= size - h; s++)
        {
            // print spce i.e. size - hash
            printf(" ");
        }
        for (s = 1; s <= h; s++)
        {
            // print hash starting 1
            printf("#");
        }

        printf("  ");

        for (s = 1; s <= h; s++)
        {
            // print hash starting 1
            printf("#");
        }
        //for (s = 1; s <= size - h; s++)
        //{
        // print spce i.e. size - hash
        //  printf(" ");
        //}

        printf("\n");
    }

}

