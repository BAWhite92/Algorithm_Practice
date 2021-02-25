def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

li = [1,3,5,76,4,3,2,21]
print(sum(li))
#recursively sum the numbers in a list, each recursion is added to the stack so
#the info is not forgotten as each item (list[0]) is removed from the list, when only
#1 number remains in the list sum() travels back up through return adding numbers together as it goes.

def items(list):
    if list == []:
        return 0
    return 1 + items(list[1:])

print(items(li))
#as each recursion is made a "1" is used to represent that item, when the last item is hit
#the recursion unwinds back up through the list and adds a 1 for each item.

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max(li))
#recursions compare item 0 of list to submax which is item 0 of the 1: slice of the list.
#each time the first nmuber is taken from list and when base case reached then the list
#will be compared from last number through to first each time carrying up the largest value.
