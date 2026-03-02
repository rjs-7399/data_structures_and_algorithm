# Print all the variables in the array and length of it

def print_all_the_variables_in_array(arr):
    print("Printing all variables in array")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")

def print_length_of_the_array(arr):
    print()
    print("Printing Length of The Array")
    print(len(arr))

def print_the_variable_with_index(array):
    print("Printing The Variable With Index")
    for i in range(0, len(array)):
        print(f"Printing variable at position {i+1}: {array[i]}")



def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_all_the_variables_in_array(array)
    print_length_of_the_array(array)
    print_the_variable_with_index(array)

if __name__ == '__main__':
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air pep_coding_functions_and_arrays_level_1 % python3 introduction_to_arrays.py
Printing all variables in array
1 2 3 4 5 6 7 8 9 10 
Printing Length of The Array
10
Printing The Variable With Index
Printing variable at position 1: 1
Printing variable at position 2: 2
Printing variable at position 3: 3
Printing variable at position 4: 4
Printing variable at position 5: 5
Printing variable at position 6: 6
Printing variable at position 7: 7
Printing variable at position 8: 8
Printing variable at position 9: 9
Printing variable at position 10: 10
"""