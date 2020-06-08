# ---------------------------------
# List

print('LIST EXAMPLE:');
names=['list-item1','list-item2','list-item3']
print(names);
print(f"List Length is: {len(names)}")
print(f"Element at Index:0=>{names[0]}")
print(f"Element at Index:1=>{names[1]}")
print(f"Element at Index:2=>{names[1]}")

names.append('list-item-4')
names.append('list-item-5')
print(names)
# ---------------------------------
# Add Item at End:

print('LIST EXAMPLE: Add Item at End');
names1=['list-item1','list-item2','list-item3']
print(names1);
names1.append('list-item-end');
print(names1);
print('\n')
# ---------------------------------
# Add Item at arbitary postion:

print('LIST EXAMPLE:Add Item at arbitary postion::');
names2=['list-item1','list-item2','list-item3']
print(names2);
names2.insert(1, 'list-item-arbitary');
print(names2);
print('\n')
# ---------------------------------
# Combine two list

print('LIST EXAMPLE:Add Item at arbitary postion::');
namesList=['khizer', 'faran']
print(namesList);
colorsList=['Black', 'White']
print(colorsList);
namesList.extend(colorsList);
print('Names List is Extended:')
print(namesList);
print('\n')
# ---------------------------------
# Varify existence of value in list

valueExistenceList = [1,2,3,4,5,1,2,3];
print('Using "in" operator')
print(f"3 in valueExistenceList, {3 in valueExistenceList}")
print(f"10 in valueExistenceList, {10 in valueExistenceList}")

# Find First Matching Result 
print('Using "index" operator')
print(f"3 in valueExistenceList, {valueExistenceList.index(3)}") 

# THIS WILL THROW ERROR WHEHRE AS "in" OPERATOR DOESN'T IF NOT EXISTS:
# print(f"10 in valueExistenceList, {valueExistenceList.index(10)}")
print('\n')
# ---------------------------------
# Count Occurence in List

countOccurencesList = [1,2,3,4,5,1,2,3];
print(f"2 Occurs, { countOccurencesList.count(2)}") 
print(f"5 Occurs, { countOccurencesList.count(5)}") 
print('\n')

# ---------------------------------

print('MODIFY/FIND FROM LIST:');
playwithList=['list-item1','list-item2','list-item3', 'find-me']
print(playwithList);
print(f"List Length is: {len(names)}")

print('Update List at Particular position')
names[0]="Modifed Data"
print(playwithList)

print('Find postion index of element')
print(playwithList)
findIdxPos=playwithList.index('find-me')

print('Replaced Data List')
playwithList[findIdxPos] = 'replace-with-me'
print(playwithList)
print('\n')

# ---------------------------------
print('REMOVE FROM LIST:');
removeFromList=['list-item1','list-item2','list-item3', 'find-me']
print(f"Original List: {removeFromList}");
removeFromList.remove("list-item1");
print("Remove First Item:")
print(removeFromList);
removeFromList.pop();
print("Remove Last Item:")
removeFromList.pop(1);
print(removeFromList);

# ---------------------------------