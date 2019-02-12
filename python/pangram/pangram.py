import string

def is_pangram(sentence):

    all_ascii = list(string.ascii_lowercase)

    sentence_low_cap = [c.lower() for c in sentence if c.isalpha()]

    for c in sentence_low_cap:
    	if c in all_ascii:
    		all_ascii.remove(c)

    return len(all_ascii) == 0

