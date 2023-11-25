#include <cs50.h>
#include <stdio.h>

int main(void)
{
   int x = get_int("What is X?");
   int y = get_int("What is Y?");

   if (x < y)
   {
        printf ("X is less is y\n");
   }
   else if (x > y)
   {
        printf ("X is not less than y\n");
   }
   else
   {
        printf ("X is equal to y\n");
   }

}