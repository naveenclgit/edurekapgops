#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int sentence = 0, word = 0, letter = 0;
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // variable to count
    int sentences = 0, words = 0, letters = 0;
    // get the text
    string mytext = get_string("Text: ");
    letters = count_letters(mytext);
    words = count_words(mytext);
    sentences = count_sentences(mytext);

    /*printf ("letter %i\n",letters);
    printf ("word %i\n",words);
    printf ("sentence %i\n",sentences);
    */

    float L = (float) letter / word * 100;
    float S = (float) sentence / word * 100;
    int gradeindex = round(0.0588 * L - 0.296 * S - 15.8);
    int gradlevel = round(gradeindex);
    //int grade = (int)(gradeindex < 0 ? (gradeindex - 0.5) : (gradeindex + 0.5));
    if (gradlevel < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (gradlevel > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", gradlevel);
    }

}

//func to count letters
int count_letters(string text)
{
    // get the length
    string mytext = text;
    int textlen = strlen(mytext);
    for (int i = 0; i < textlen; i++)
    {
        if (isalpha(mytext[i]))
        {
            letter++ ;
        }
    }
    return letter;
}

// Func to count words, even in double quotes
int count_words(string text)
{
    string mytext = text;
    int textlen = strlen(mytext);
    for (int i = 0; i < textlen; i++)
    {
        if ((i == 0 && isalpha(mytext[i])) || (isspace(mytext[i - 1]) && isalpha(mytext[i])) || (mytext[i - 1] == 34 && isalpha(mytext[i])))
        {
            word++;
            // printf ("%i is %c \n ", word, mytext[i]);
        }
    }
    return word;
}

//func to count sentenses 
int count_sentences(string text)
{
    string mytext = text;
    int textlen = strlen(mytext);
    for (int i = 0; i < textlen; i++)
    {
        if (mytext[i] == '.' || mytext[i] == '!' || mytext[i] == '?')
        {
            sentence++;
        }
    }
    return sentence;
}