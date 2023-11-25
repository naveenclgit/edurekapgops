#include <stdio.h>


int main(void)
{
    int i = 50;
    int *p = &i;
    printf("%p\n", p);
    printf("%p\n", &i);
    printf("%i\n", *p);

    char *name="Naveen";
    printf("%p\n", name);
    printf("%p\n", &name[0]);
    printf("%s\n", name+2);

    int a = 28;
    int b = 50;
    printf("a has value %i, located at %p\n", a ,&a);
    printf("b has value %i, located at %p\n", b ,&b);

    int *c = &a;
    *c = 14;
    printf("c has inter value %p, located at %p\n", c ,&c);
    c = &b;
    *c = 25;
    printf("a has value %i, located at %p\n", a ,&a);
    printf("b has value %i, located at %p\n", b ,&b);
    printf("c has value %p, located at %p\n", c ,&c);
    FILE *input = fopen("myfile.txt","w");
    fprintf(input, "a has value %i, located at %p\n", a ,&a);
    fprintf(input, "b has value %i, located at %p\n", b ,&b);
    fprintf(input, "c has value %p, located at %p\n", c ,&c);
    fclose(input);
}