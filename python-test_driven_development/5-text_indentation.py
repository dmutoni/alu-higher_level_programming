#!/usr/bin/python3
''' Defining a text indentation function that prints indented text '''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after . ? and :
    Ensures text is a string
    Raises an error if text is not a string
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("\n")
        elif text[i] == " ":
            for x in range(i, 0, -1):
                if text[x] == " ":
                    continue
                elif text[x] in [".", "?", ":"]:
                    break
                else:
                    print(text[i], end="")
                    break
        else:
            print(text[i], end="")
