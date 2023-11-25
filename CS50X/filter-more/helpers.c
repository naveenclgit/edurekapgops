#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int myvert = 0; myvert < height; myvert++)
    {
        for (int myhorz = 0 ; myhorz < width; myhorz++)
        {
            // make it grayscale by average of color
            int colorval = round((image[myvert][myhorz].rgbtRed + image[myvert][myhorz].rgbtGreen + image[myvert][myhorz].rgbtBlue) / 3.0);
            image[myvert][myhorz].rgbtRed = colorval;
            image[myvert][myhorz].rgbtGreen = colorval;
            image[myvert][myhorz].rgbtBlue = colorval;

        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    for (int myvert = 0; myvert < height; myvert++)
    {
        for (int myhorz = 0 ; myhorz < width / 2 ; myhorz++)
        {
            // Get the pixel to a variable
            RGBTRIPLE mytmp = image[myvert][width - 1 - myhorz];
            image[myvert][width - 1 - myhorz] = image[myvert][myhorz];
            image[myvert][myhorz] = mytmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE mytmp[height][width];
    double red, green, blue;
    int mycount = 0;
    int mybokx = 1;

    for (int myvert = 0; myvert < height; myvert++)
    {
        for (int myhorz = 0; myhorz < width; myhorz++)
        {
            red = 0;
            green = 0;
            blue = 0;
            mycount = 0;
            // Loop around current pixel top left to bottom right
            for (int row = myvert - mybokx; row <= myvert + mybokx; row++)
            {
                for (int col = myhorz - mybokx; col <= myhorz + mybokx; col++)
                {
                    if ((row >= 0 && row < height) && (col >= 0 && col < width))
                    {
                        // Update average count and add the color values to the existing averages
                        blue += image[row][col].rgbtBlue;
                        green += image[row][col].rgbtGreen;
                        red += image[row][col].rgbtRed;
                        mycount++;
                    }
                }
            }
            // Average color values and paint temp image
            blue =  round(blue / (double) mycount);
            green = round(green / (double)  mycount);
            red = round(red / (double) mycount);
            mytmp[myvert][myhorz].rgbtBlue = blue;
            mytmp[myvert][myhorz].rgbtGreen = green;
            mytmp[myvert][myhorz].rgbtRed = red;
        }
    }
    // Loop through each pixel and replace original image with modified temp image
    for (int myvert = 0; myvert < height; myvert++)
    {
        for (int myhorz = 0; myhorz < width; myhorz++)
        {
            image[myvert][myhorz] = mytmp[myvert][myhorz];
        }
    }


    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE mytmp[height][width];
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    int mybokx = 1;
    // copy the image to tmpimge pxl by pxl
    for (int myvert = 0; myvert < height; myvert++)
    {
        for (int myhorz = 0; myhorz < width; myhorz++)
        {
            mytmp[myvert][myhorz] = image[myvert][myhorz];
        }
    }


    for (int myvert = 0; myvert < height; myvert++)
    {
        for (int myhorz = 0; myhorz < width; myhorz++)
        {
            // repaint xy color on  pixel
            float redx = 0,  greenx = 0, bluex = 0, redy = 0, greeny = 0, bluey = 0;
            // Loop around current pixel top left to bottom right
            for (int row = -1; row < 2; row++)
            {
                for (int col = -1; col < 2; col++)
                {
                    if (myvert + row < 0 || myvert + row >= height || myhorz + col < 0 || myhorz + col >= width)
                    {
                        continue;
                    }
                    // multiply image values to weighted sums
                    redx   += mytmp[myvert + row][myhorz + col].rgbtRed   * Gx[row + 1][col + 1];
                    greenx += mytmp[myvert + row][myhorz + col].rgbtGreen * Gx[row + 1][col + 1];
                    bluex  += mytmp[myvert + row][myhorz + col].rgbtBlue  * Gx[row + 1][col + 1];
                    redy   += mytmp[myvert + row][myhorz + col].rgbtRed   * Gy[row + 1][col + 1];
                    greeny += mytmp[myvert + row][myhorz + col].rgbtGreen * Gy[row + 1][col + 1];
                    bluey  += mytmp[myvert + row][myhorz + col].rgbtBlue  * Gy[row + 1][col + 1];
                }
            }
            int combineRed = round(sqrt((redx * redx) + (redy * redy)));
            int combineGreen = round(sqrt((greenx * greenx) + (greeny * greeny)));
            int combineBlue = round(sqrt((bluex * bluex) + (bluey * bluey)));
            // Max to at 255
            if (combineRed > 255)
            {
                combineRed = 255;
            }
            if (combineGreen > 255)
            {
                combineGreen = 255;
            }
            if (combineBlue > 255)
            {
                combineBlue = 255;
            }
            image[myvert][myhorz].rgbtRed = combineRed;
            image[myvert][myhorz].rgbtGreen = combineGreen;
            image[myvert][myhorz].rgbtBlue = combineBlue;
        }
    }
    return;
}
