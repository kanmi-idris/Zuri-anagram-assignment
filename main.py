# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

        # the sorted strings are checked
    if(sorted(word)== sorted(anagram)):
        print("True")
    else:
        print("False")

word ="listen"
anagram ="silent"
find_anagram(word, anagram)