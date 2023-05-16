def move_to_end(lst):
    #creating two empty lists to classify duplicate and non duplicate items
    duplicates = []		
    non_duplicates = []	
    #creating a loop to add duplicate items to duplicate lsits and non duplicate itmes to no duplicate list
    for item in lst:
        if lst.count(item) > 1:
            duplicates.append(item)
        else:
            non_duplicates.append(item)
    #creating a loop to Remove all the duplicate items from the main list
    for duplicate in duplicates:
        lst.remove(duplicate)  
    #adding duplicate items to the end of the list
    lst.extend(duplicates)
    #adding a if statement to counter when no duplicate items are present 
    if duplicates == []:
        print("No duplicate found !")
    return lst

lst = eval(input("enter your list:"))
new_list = move_to_end(lst)
print(new_list)
