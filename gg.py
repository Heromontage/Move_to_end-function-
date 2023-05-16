def move_to_end(lst):
    duplicates = []		
    non_duplicates = []	
    for item in lst:
        if lst.count(item) > 1:
            duplicates.append(item)
        else:
            non_duplicates.append(item)
    for duplicate in duplicates:
        lst.remove(duplicate)        
    lst.extend(duplicates)
    if duplicates == []:
        print("No duplicate found !")
    return lst

lst = eval(input("enter your list:"))
new_list = move_to_end(lst)
print(new_list)