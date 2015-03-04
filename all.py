# -*- coding: utf-8 -*-
"""
Gregor Ulm
2015-03-04
Jeppesen Gestumblindi Coding Challenge

Python 2.7
"""


def readFile(filename):
    """Reads dictionary file

    Args:
        filename: the name of the dictionary file.
    Returns:
        A dictionary with separate keys for all words of a given length.
    """
    
    myDict = { key:[] for key in range(1, 20) }
    
    with open(filename, "r") as f: # file is closed automatically due to 'with'
        for word in f:
            word = word.strip()    # remove white space
            if len(word) > 19:     # we won't need those
                continue
            myDict[len(word)].append(word)
           
    return myDict
            

def isContained(word, phrase):
    """Checks whether 'word' is contained in 'phrase'
    
    This is a very fast way of determining whether a word that is contained
    in the dictionary can be formed by a permutation of the letters of the
    provided phrase. Note that both the word and the phrase have to be
    supplied as 'sorted' strings.
    
    To illustrate the recursion:
        1) Base case: word == "": all letters were found in 'phrase'; thus it
            matches.
        2) Base case: phrase == "": there were letters in 'word' that were not
            contained in 'phrase', thus this word has to be rejected.
        3) Recursive case: if the first letters of both 'word' and 'phrase'
            match, the remainder of both has to be checked.
        4) Recursive case: if the first letter of 'word' does not match the
            first letter of 'phrase', then the rest of phrase has to be checked.
            Note that this only works because both strings are sorted.
        
        Example:
                word: "abbce", phrase: "aaabbce"
                The first letter matches, thus the recursive call is:
                isMatch("bbce", "aabbce")
                
                now there are several mismatches in a row, leading to these
                calls:
                    
                isMatch("bbce", "abbce")
                isMatch("bbce", "bbce")
                
                From there, the base case can easily be reached.
                       
    Args:
        word: the 'sorted' dictionary word that is going to be looked up
        phrase: the 'sorted' phrase  
    Returns:
        A Boolean value indicating whether 'word' is contained in 'phrase'.
    """
    
    if word == "":
        return True
    
    if phrase == "":
        return False
    
    if word[0] == phrase[0]:
        return isContained(word[1:], phrase[1:])
    else:
        return isContained(word, phrase[1:])
        
      
def getMatches(wordList, phrase):
    """Determines all matching words

    Args:
        wordList: all words of a given length n
        phrase:   the 'sorted' phrase
        
    Returns:
        A list of all dictionary words that are contained in the given phrase.
    """    

    result = []
    for word in wordList:
        wordSorted = ''.join(sorted(word))
        if isContained(wordSorted, phrase):
            result.append(word)
           
    return result
       

def main():
    filename = "words.txt"
    phrase   = "optimizationmatters"
    
    phrase   = ''.join(sorted(phrase))
    myDict   = readFile(filename)
            
    for n in range(1, 20):       
        wordsOfLengthN = myDict[n]   
        matches        = getMatches(wordsOfLengthN, phrase)    
        print "=" * 50 + "\n"
        print "All matches for word length " + str(n)
        print "Total: " + str(len(matches))
        print matches
        
        # uncomment to write results to files
        """
        target = open("results/" + str(n) + ".txt", 'w')
        target.write(str(len(matches)) + "\n")
        for element in matches:
            target.write(element)
            target.write("\n")
        target.close()
        """
main()


# test cases for the most relevant function
def tests():
    assert isContained("", "a")
    assert not isContained("a", "")
    assert not isContained("abc", "acb")
    assert isContained("abc", "abc")
    assert isContained("abcde", "abcdef")