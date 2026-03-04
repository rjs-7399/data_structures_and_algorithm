def difference_of_two_arrays(arr1, arr2):
    arr3 = []
    if len(arr1) > len(arr2):
        arr2 = [0]*(len(arr1)-len(arr2)) + arr2
    elif len(arr2) > len(arr1):
        arr1 = [0]*(len(arr2)-len(arr1)) + arr1

    for i in range(len(arr1)-1, -1, -1):
        if arr1[i] < arr2[i]:
            arr1[i-1] = arr1[i-1] - 1
            arr3.append(arr1[i] + 10 - arr2[i])
            print(f"Value at current index {i} is {arr1[i] + 10 - arr2[i]}")
        else:
            arr3.append(arr1[i] - arr2[i])
            print(f"Value at current index {i} is {arr1[i] - arr2[i]}")
    final_arr = arr3[::-1]

    while len(final_arr) > 1 and final_arr[0] == 0:
        final_arr.pop(0)
    return final_arr


def main():
    print("Two input arrays:")
    arr1 = [8,0,5,4,3,2]
    arr2 = [4,6,8,7,5,9]
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print()
    print("Debugging the Process:")
    result = difference_of_two_arrays(arr1, arr2)
    print("\nDifference of two arrays:")
    print(result)

if __name__ == '__main__':
    main()

"""
(basevenv) rutvikshah@Rutviks-MacBook-Air video_26_27 % python3 difference_of_two_arrays.py
Two input arrays:
Array 1: [8, 0, 5, 4, 3, 2]
Array 2: [4, 6, 8, 7, 5, 9]

Debugging the Process:
Value at current index 5 is 3
Value at current index 4 is 7
Value at current index 3 is 6
Value at current index 2 is 6
Value at current index 1 is 3
Value at current index 0 is 3

Difference of two arrays:
[3, 3, 6, 6, 7, 3]
"""