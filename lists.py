# lists.py

# lists, sets, tuples, dictionaries
# list = sorted and changeable data structures, where duplicates are allowed

a_list = ["this", "is", "a", "list"]
print(a_list)

print(a_list[0])

# change list

a_list[2] = "no"
print(a_list)

# check list for values with if...in
if "no" in a_list:
    print("this is supposed to not be a list", type(a_list))

print(len(a_list))

# extend list
a_list.append('test')
print(a_list)

a_list.remove('test')
print(a_list)

# another removal command: pop

a_list.pop()
print(a_list)

# empty list

a_list.clear()
print(a_list)