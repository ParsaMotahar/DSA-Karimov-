'''Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

    myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
    first_second(myList) # 90 87'''
scores = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
def first_second(scores):
    scores.sort()
    return scores[len(scores)-2:len(scores)]
print(first_second(scores))