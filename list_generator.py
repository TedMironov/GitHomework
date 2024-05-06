from list_generator import generate_list

def fill_list_element_by_element(n):
    lst = generate_list(n)
    for i in range(len(lst)):
        lst[i] = int(input(f"Enter element {i+1}: "))
    return lst

n = int(input("Enter the length of the list: "))
result = fill_list_element_by_element(n)
print("Final list:", result)