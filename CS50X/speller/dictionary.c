// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int wrdcnt = 0;


// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashval = hash(word);
    node *headval = table[hashval];

    while (headval != NULL)
    {
        //check word
        if (strcasecmp(headval->word, word) == 0)
        {
            return true;
        }
        headval = headval->next;

    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // open the file
    FILE *srcfile = fopen(dictionary, "r");
    if (srcfile == NULL)
    {
        return false;
    }

    // Get the words
    char strwrd[LENGTH + 1];

    while (fscanf(srcfile, "%s", strwrd) != EOF)
    {
        //allocate memory
        node *mytmp = malloc(sizeof(node));

        if (mytmp == NULL)
        {
            return false;
        }

        // copy words and get hash val
        strcpy(mytmp->word, strwrd);
        int hashval = hash(strwrd);

        if (table[hashval] == NULL)
        {
            mytmp->next = NULL ;
        }
        else
        {
            mytmp->next = table[hashval];
        }
        table[hashval] = mytmp;

        wrdcnt++;
    }
    fclose(srcfile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wrdcnt;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *freewd = table[i];

        while (freewd != NULL)
        {
            node *tmpfreewd = freewd->next;
            free(freewd);
            freewd = tmpfreewd;

        }
        if (freewd == NULL && i == N - 1)
        {
            return true;
        }

    }

    return false;
}
