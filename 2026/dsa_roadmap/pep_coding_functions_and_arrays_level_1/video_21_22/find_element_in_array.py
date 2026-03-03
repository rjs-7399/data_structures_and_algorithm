def find_element_in_array(arr, k):
    index = -1
    for i in range(0, len(arr)):
        if arr[i] == k:
            index = i
            break
    return index

def main():
    arr = [6, 15, 30, 40, 4, 11, 9, 40]
    k = 40
    print("Given array is")
    print(arr)
    index = find_element_in_array(arr, k)
    print(f"Index of element {k} in given arr is: {index}")

if __name__ == "__main__":
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air video_21_22 % python3 find_element_in_array.py 
Given array is
[6, 15, 30, 40, 4, 11, 9, 40]
Index of element 40 in given arr is: 3
"""
