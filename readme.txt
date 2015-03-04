Gregor Ulm
2015-03-04
Jeppesen: Gestumblindi Coding Challenge

Python 2.7



Text of the Problem

Gestumblindi has been busy learning Java. No mean feat for a mythological
character. In this challenge he’s throwing down the gauntlet and challenging you
to get coding.

He wants you to write an application in the language of your choice. It should
take the term “optimizationmatters” and generate a list and count of all
possible 3 letter words contained within an English dictionary. If you want to
show off your optimization skills how about generating all possible words for
length 1 up to 19? At Jeppesen we are passionate about clean, well-tested and
optimized code so keep that in mind when creating your solution.



Files

three.py: A straightforward implementation that returns all matching words of
length 3.  The two main optimizations are described in the comments. This
The used approach works very well for the given problem, but does not scale
to longer words, due to the fact that the generation of permutations is O(n!).

all.py: An optimized solution that finds all matching words of length 1 to 19.
The results are printed on the screen, and optionally stored in the directory
/results. This solution is fast, with the bottleneck apparently being
printing to the screen.

words.txt: This is a file containing well over 100,000 words of the English
language, the so-called Enable list of the Scrabble community. Note that this
list has been placed in the public domain.
http://www.puzzlers.org/dokuwiki/doku.php?id=solving%3awordlists%3aabout%3astart
http://www.puzzlers.org/pub/wordlists/enable1.txt