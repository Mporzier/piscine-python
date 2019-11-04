import sys
import string


def text_analyzer(txt=''):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if not txt:
        print("What is the text to analyze ?")
        print(">> ", end='')
        txt = input()
    print("The text contains", len(txt), "characters:")
    print("- ", sum(1 for c in txt if c.isupper()), "upper letters")
    print("- ", sum(1 for c in txt if c.islower()), "lower letters")
    print("- ", sum(1 for c in txt if string.punctuation.find(c) != -1),
          "punctuation marks")
    print("- ", sum(1 for c in txt if c.isspace()), "spaces")
