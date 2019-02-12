import string


def hey(phrase: str) -> str:

    """
    The function takes a string input, and returns a string response, based on the content of the input.
    """

    clean_phrase = phrase.strip()
    all_letters = [i for i in clean_phrase if i in string.ascii_letters]
    all_uppercase_letters = [i for i in clean_phrase if i in string.ascii_uppercase]

    if len(clean_phrase) == 0:
        return "Fine. Be that way!"

    elif len(all_letters) == len(all_uppercase_letters) and len(all_letters) != 0:
        if clean_phrase.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"

    elif clean_phrase.endswith("?"):
        return "Sure."

    else:
        return "Whatever."

