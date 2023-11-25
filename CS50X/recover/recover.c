#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define BLOCK_SIZE 512

typedef uint8_t  BYTE;

int main(int argc, char *argv[])
{

    //Enforce valid usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    //open argv file
    char *ifile = argv[1];
    FILE *infile = fopen(ifile, "r");
    FILE *otfile = NULL;
    // check for file
    if (infile == NULL)
    {
        fprintf(stderr, "Cound't open %s \n", ifile);
        printf("Cound't open %s \n", ifile);
        return 2;
    }
    // Check the start  JPEG file its - 0xff 0xd8 0xff 0xeX
    BYTE bufptr[BLOCK_SIZE];
    int mycount = 0;
    int countwrite = 0;
    // Loop and read file by 512 bytes
    while (fread(&bufptr, 1, BLOCK_SIZE, infile) == BLOCK_SIZE)
    {
        if (bufptr[0] == 0xff && bufptr[1] == 0xd8 && bufptr[2] == 0xff && (bufptr[3] & 0xf0) == 0xe0)
        {
            if (countwrite == 1)
            {
                // close previous file, as new start
                fclose(otfile);
            }
            else
            {
                countwrite = 1;
            }
            //start new file write
            char myfile[8];
            sprintf(myfile, "%03i.jpg", mycount);
            otfile = fopen(myfile, "w");
            mycount++;

        }
        //keep wrtiging
        if (countwrite == 1)
        {
            fwrite(&bufptr, 1, BLOCK_SIZE, otfile);
        }

    }
    fclose(infile);
    fclose(otfile);
}