# -*- coding: utf-8 -*-
"""
Gregor Ulm
2015-03-04
Jeppesen: Gestumblindi Coding Challenge

Python 2.7
"""

from itertools import permutations
from bisect    import bisect_left


def readFile(filename):
    """Reads dictionary file

    Args:
        filename: the name of the dictionary file.
    Returns:
        A list of words of length 3.
    """
    
    result = []
    
    with open(filename, "r") as f: # file is closed automatically due to 'with'
        for word in f:
            newWord = word.strip()      # remove white space
            if len(newWord) == 3:       # we only need those
                result.append(newWord)  
           
    result.sort()
    return result


def getUniquePermutations(phrase, n):
    """Computes unique permutation

    Args:
        phrase: String to be permuted
        n:      number of letters to chose from 'phrase'
            
    Returns:
        All unique permutations given 'n' and 'phrase'.
    """
    assert n > 0 and n < len(phrase)
    
    result = []
    for c in permutations(phrase, n):
        result.append(''.join(list(c)))  # convert tuple to string and append
   
    return list(set(result))    # to remove duplicates 
"""
Optimization: Excluding duplicates

For instance, when choosing three letters from the given phrase, there are
19 * 18 * 17 = 5814 combinations. However, with the given input phrase, there
are only 1142 unique combinations.
"""
   
   
def getMatches(combinations, words):
    """Computes all matching words
    
    Given a (sorted) list of words, and a list of combinations of letters,
    this function computes the intersection of these two lists.

    Args:
        combinations: All three letter permutations of 'phrase'.
        words:        All three letter words in the dictionary.
            
    Returns:
        All combinations that are also found in 'words'.
    """
    
    # cf. 8.5.1 at https://docs.python.org/2/library/bisect.html
    def index_bisect(words, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect_left(words, x)
        if i != len(words) and words[i] == x:
            return i
        return -1  
        
    result = []
    # efficiently compute the intersection of both lists:
    for c in combinations:
        if index_bisect(words, c) != -1:
            result.append(c)
                                          
    return result  
"""
Optimization: Improve lookup from O(n) to O(log n)

When constructing the list that contains all three-letter words, the order is
determined by the order of the text file that was used as input. A relatively
straightforward optimization consists of sorting that list, and then using
binary search for the lookup. Given that a large number of permutations of
‘phrase’ are not actual English words, an unsorted list would hit the worst
case of O(n) frequently.

However, by ordering the list of values, binary search can be used to look up
potential words, which happens in O(log n).
"""

    
def main():    
    filename   = "words.txt"
    phrase     = "optimizationmatters"
    
    myDict     = readFile(filename)  # this list is sorted
    wordLength = 3
    
    uniques    = getUniquePermutations(phrase, wordLength)  
    result     = getMatches(uniques, myDict) 
    
    print "Number of matches: " + str(len(result))
    print result

main()


# test cases for the most relevant functions
def tests():
    assert getMatches([], [])                 == []
    assert getMatches(["a", "b"], [])         == []
    assert getMatches([], ["a", "b"])         == []
    assert getMatches(["a", "b"], ["b", "c"]) == ["b"]
    
    list1 = getUniquePermutations("abcde", 3)
    list2 = getUniquePermutations("acdeb", 3)
    list1.sort()
    list2.sort()
    assert list1 == list2 