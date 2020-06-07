# Mutable List Example:
def create_mutable_list(value1, list=[]):
    list.append(value1)
    print(list)
    
create_mutable_list(10)
create_mutable_list(20)

# Immutable List Example:
def create_immutable_list(value1, list=None):
    if(list is None):
        list=[]
    list.append(value1)
    print(list);
    
create_immutable_list(10)
create_immutable_list(20)
