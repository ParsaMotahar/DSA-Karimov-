'''Count Word Frequency

Define a function to count the frequency of words in a given list of words.

Example:

    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
    count_word_frequency(words) 

Output:

     {'apple': 3, 'orange': 2, 'banana': 1}'''

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def count_word_frequency(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
print(count_word_frequency(words))
