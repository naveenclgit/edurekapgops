#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    string myword = word;
    int wordlen = strlen(word);
    int myscore = 0;

    // looping thru the each char in the string
    for (int i = 0 ; i < wordlen; i++)
    {
        // checking if its a letter
        // if (myword[i] >= 65 && myword[i] <= 122)
        if (isalpha(myword[i]))
        {
            char mychar = myword[i];
            if (mychar == 65 || mychar == 97 || mychar == 69 || mychar == 101 || mychar == 73 || mychar == 105 || mychar == 76 || mychar == 108
                || mychar == 78 || mychar == 110 || mychar == 79 || mychar == 111 || mychar == 82 || mychar == 114 || mychar == 83 || mychar == 115
                || mychar == 84 || mychar == 116 || mychar == 85 || mychar == 117)
            {
                // 1 pointers
                myscore = myscore + 1;
            }
            else if (mychar == 68 || mychar == 100 || mychar == 71 || mychar == 103)
            {
                // 2 pointers
                myscore = myscore + 2;
            }
            else if (mychar == 66 || mychar == 98 || mychar == 67 || mychar == 99 || mychar == 77 || mychar == 109 || mychar == 80
                     || mychar == 112)
            {
                // 3 pointers
                myscore = myscore + 3;
            }
            else if (mychar == 70 || mychar == 102 || mychar == 72 || mychar == 104 || mychar == 86 || mychar == 118 || mychar == 87
                     || mychar == 119 || mychar == 89 || mychar == 121)
            {
                // 4 pointers
                myscore = myscore + 4;
            }
            else if (mychar == 74 || mychar == 106 || mychar == 88 || mychar == 120)
            {
                // 8 pointers
                myscore = myscore + 8;
            }
            else if (mychar == 75 || mychar == 107)
            {
                // 5 pointers
                myscore = myscore + 5;
            }
            else if (mychar == 81 || mychar == 113 || mychar == 90 || mychar == 122)
            {
                // 10 pointers
                myscore = myscore + 10;
            }

        }
        else
        {
            // no points for non alphabetic chars 
            myscore  = myscore + 0;
        }
    }

    return myscore;

}
