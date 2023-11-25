#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int myhorz = 0 ; myhorz < width; myhorz++)
    {
        for (int myvert = 0; myvert < height; myvert++)
        {
            // make all blacks 000 to A red based color.
            if (image[myvert][myhorz].rgbtRed == 0 && image[myvert][myhorz].rgbtGreen == 0 && image[myvert][myhorz].rgbtBlue == 0)
            {
                image[myvert][myhorz].rgbtRed = 125;
                image[myvert][myhorz].rgbtGreen = 15;
                image[myvert][myhorz].rgbtBlue = 25;

            }
            // make all whites to blacks. 
            else if (image[myvert][myhorz].rgbtRed == 255 && image[myvert][myhorz].rgbtGreen == 255 && image[myvert][myhorz].rgbtBlue == 255)
            {
                image[myvert][myhorz].rgbtRed = 0;
                image[myvert][myhorz].rgbtGreen = 0;
                image[myvert][myhorz].rgbtBlue = 0;
            }

        }
    }

}
