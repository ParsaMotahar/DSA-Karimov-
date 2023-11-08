word1 = input("Enter a word:\n").lower()
word2 = input("Enter another word:\n").lower()
def IsPermutation(word1, word2):
    word1List = [c for c in word1]
    word2List = [a for a in word2]
    word1List.sort()
    word2List.sort()
    if word1List == word2List:
        return True
    else:
        return False
print()
print(IsPermutation(word1, word2))