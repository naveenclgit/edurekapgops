#include <cs50.h>
#include <stdio.h>

int main(void)
{
   string first = get_string("Whats is your first name? ");
   string last = get_string("What is your last name? ");
   int age = get_int("What is your age?");
   string phone = get_string("What is your Phone? ");

   printf("Age is %i. Name is %s,%s. Phone number is  %s. \n", age,last,first,phone);

}