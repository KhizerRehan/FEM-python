# Sets
# - Set is Mutable You can add/remove
# - Contains Unique Values
# - Values Can't be Accessing usning Index Positions.
# - Set doesn't maintain Order.


print(type({})) # dict type
set() # create an empty set
{1} # add value in sets
print(type({2}))

# Set Doesn't cotaine duplicate values
names={'Khizer', 'Faran', 'Khizer'}
print(names)
print(f"Length in Set is of Unique Values {len(names)}")

# Set doesn't contain Order
my_set={1,"a",2,"b", "cat"}
type(my_set)
print(my_set)

# Sets doesn't support indexing e.g like in Arrays
# my_set[0] => Will Throw an error

# -----------------------
colors={"Red", "Yellow", "Pink", "Green"}
print(f"Colors Set is,{colors}")
colors.discard('Yellow');
print(f"Colors Set After Discard is,{colors}")
colors.discard('Purple')  # NO ERROR WILL BE THROWN.
print(f"LIST IS SAME EVEN AFTER DISCARD OF NON-EXISTENCE ITEM: {colors}")
colors.remove('Pink');
print(f"Colors Set After Remove is,{colors}")
# colors.remove('Purple'); THIS WILL THROW AN ERROR.


# -----------------------
print("Combine Sequence")
numbers={1,2,3,4}
colors.update(numbers)
print(f"Combine two Sets {colors}")

fname={'khizer'}
lname={'rehan'}
fname.update(lname)
print(f"Fullname is {fname}")

pass_single_string = 'Splitted'
set_will_split_under_the_hood=set(pass_single_string)

# Look Order is not maintained too SET DOESN'T MAINTAIN ORDER:
print(set_will_split_under_the_hood)
# -----------------------
# Union / Intersection / Difference

my_favourite_colors={"Red","Blue", "Black"}
yours_favourite_colors={"Pink","Blue", "Black"}
print(my_favourite_colors)
print(f"My Favourite Colors", my_favourite_colors)
print(f"Your Favourite Colors", yours_favourite_colors)
print(f"Union,{ my_favourite_colors | yours_favourite_colors }")
print(f"Intersection,{ my_favourite_colors & yours_favourite_colors }")
print(f"Difference,{ my_favourite_colors ^ yours_favourite_colors }")

# -----------------------
# - Little hack to convert set to list so that you can sort 
# because set cannot be sorted
print(f"Default Sort Set Into List {sorted(list(yours_favourite_colors))}")
print(f"Reverse Sort Set Into List {sorted(list(yours_favourite_colors), reverse= True)}")