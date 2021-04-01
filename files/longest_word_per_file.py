import os


def cleanup_word(word: str) -> str:
    """Remove extraneous tokens from word"""
    for token in [',', '.', '.', ')', '"']:
        word = word.replace(token, '')
    return word

def find_longest_word(fname: str) -> str:
    """takes a filename as an argument and returns the longest word found in the file"""
    longest_word = ''
    with open(fname) as f:
        for line in f.readlines():
            # lowercase all words
            for word in line.lower().split():
                # skip hyphenated words and repeated characters, like a horizontal line
                if '-' in word or '—' in word or '&mdash' in word or len(set(word)) == 1:
                    continue
                # parse word to remove tokens
                parsed_word = cleanup_word(word)
                if len(parsed_word) > len(longest_word):
                    longest_word = parsed_word
    return longest_word

def find_all_longest_words(directory: str) -> dict:
    """takes a directory name and returns a dict in which the keys are filenames and
    the values are the longest words from each file."""
    return {fname: find_longest_word(os.path.join(directory, fname)) for fname in os.listdir(directory)}
