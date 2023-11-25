# ref  me50 / users / naveenclgit / cs50 / problems / 2023 / x / readability
import math

sentence = 0
word = 0
letter = 0


# for count of letters
def count_letters(text):
    mytext = text
    textlen = len(mytext)
    for i in range(textlen):
        if mytext[i].isalpha():
            global letter
            letter += 1
    return letter


# for count of words
def count_words(text):
    mytext = text
    textlen = len(mytext)
    global word
    word = len(mytext.split())
    return word


# for count of sentences
def count_sentences(text):
    mytext = text
    textlen = len(mytext)
    global sentence
    sentence = mytext.count('.') + mytext.count('!') + mytext.count('?')
    return sentence


def main():
    sentences = 0
    words = 0
    letters = 0
    mytext = input("Text: ")
    letters = count_letters(mytext)
    words = count_words(mytext)
    sentences = count_sentences(mytext)
    L = (float)(letter / word * 100)
    S = (float)(sentence / word * 100)
    # Coleman-Liau index
    gradeindex = round(0.0588 * L - 0.296 * S - 15.8)
    gradlevel = round(gradeindex)
    if gradlevel < 1:
        # if lower than 1
        print("Before Grade 1")
    elif gradlevel > 16:
        # higher than 16
        print("Grade 16+")
    else:
        # actual grade level 
        print("Grade", gradlevel)


if __name__ == "__main__":
    main()