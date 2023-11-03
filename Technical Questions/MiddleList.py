'''Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
    '''
MyList = [1,2,3,4,5]
def RemoveFirstAndLast(lis):
    del lis[0]
    del lis[len(lis)-1]
    print(lis)
RemoveFirstAndLast(MyList)