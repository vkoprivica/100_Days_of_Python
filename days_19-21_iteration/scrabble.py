import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/Users/Vule/Documents/Python/PyBites/dictionary.txt')
# urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


letters = "G, A, R, Y, T, E, V".split(",")
def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    # valid_words = [word for word in _get_permutations_draw(draw) if word in dictionary]
    # return valid_words
    return [word for word in _get_permutations_draw(draw) if word in dictionary]
   


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    all_permutations = []
    for length in range (7):
        all_permutations.extend([''.join(word).lower()
                         for word in itertools.permutations(draw, length)])
    return all_permutations
    # return [("".join(letter).lower()).replace(" ", "") for letter in itertools.permutations(letters, 6)]
    

if __name__ == "__main__":
    print(get_possible_dict_words(letters))
    # print(_get_permutations_draw(letters))
    # print(type(dictionary))
   

   