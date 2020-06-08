
# Built In Sort List
# This way of sorting is like ByValue not by Ref doesn;t update original list

print('SORTING EXAMPLE:');

sortMyList=[1,2,3,4,5]
print(sortMyList);

print('NORMAL SORT');
print(sorted(sortMyList))

print('REVERSE SORT');
print(sorted(sortMyList, reverse=True))

print('ORIGINAL ORDER OF LIST IS RETAINED');
print(sortMyList)
# -----------------------------------

# Second way of Sorting:
# This way of sorting is like ByRef Updates underlying list

print('SORTING EXAMPLE METHOD-2:');
sortMyList=[1,2,3,4,5]
print('NORMAL SORT LIST');
print(sortMyList.sort())

print('REVERSE SORT LIST');
print(sortMyList.reverse())

print('ORIGINAL ORDER OF LIST IS "NOT" RETAINED');
print(sortMyList)

# -----------------------------------