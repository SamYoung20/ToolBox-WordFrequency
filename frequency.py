import string
import requests

beautiful_text = requests.get('http://www.gutenberg.org/cache/epub/9830/pg9830.txt').text


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    exclude = set(string.punctuation)  # makes set of punctuation characters
    file1 = file_name
    s = ''.join(ch for ch in file1 if ch not in exclude)   # for each character of the story creates a new string without any of the pucntiation
    startBook = s.index('CHAPTER I') + 9
    s = s.lower()
    s = s[startBook:]
    lis_File = s.split() # breaks up string at the spaces creates a list of elements
    return lis_File


get_word_list(beautiful_text)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    words = word_list
    word_freq = dict()
    for c in words:
        word_freq[c] = word_freq.get(c, 0) + 1  # counts the number of times eeach word appears and keeps track in dictioary
    freqsorted = sorted(word_freq, key=word_freq.__getitem__, reverse=True)  # sorts dictionary by value (by frequency of word in story) highest value first
    print(freqsorted[:n])
    return freqsorted[:n]  # returns the first 10 words


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    get_top_n_words(get_word_list(beautiful_text), 100)
