'''Duplicate Number

Write a function to remove the duplicate numbers on given integer array/list.

Example

    remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    Output : [1, 2, 3, 4, 5]'''

MyList = [1,1,1,1,1,2,2,3,4,4,4,4,4,5]
def remove_duplicates(MyList):
    for i in MyList:
        appears = MyList.count(i)
        if appears > 1:
            for cycles in range(appears-1):
                MyList.remove(i)
        else:
            continue
    return MyList
print(remove_duplicates(MyList))


'''Please note I did it this way to see if it works
I think I know an easier way to do this.
It involves just making a new list lol. I think the 
time complexity is better but the space
complexity is worse'''