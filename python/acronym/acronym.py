import re

def abbreviate(words):
    '''
    The function takes a string of words and return their uppercase initials as one word.
    :param words: string of words
    :return: string acronym of input words
    '''
    words_with_no_apo = re.sub(pattern=r"'", repl="", string=words)
    words_with_letters_only = re.sub(pattern=r"[\W]|[_]", repl=" ", string=words_with_no_apo)
    words_as_list = words_with_letters_only.split()
    upper_initials = [word[0].upper() for word in words_as_list]
    return "".join(upper_initials)



