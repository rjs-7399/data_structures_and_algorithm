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
        print()
    final_arr = arr3[::-1]

    while len(final_arr) > 1 and final_arr[0] == 0:
        final_arr.pop(0)
    return final_arr


def main():
    arr1 = [9,9,9]
    arr2 = [9,9,9]
    ans = difference_of_two_arrays(arr1, arr2)
    print(ans)

if __name__ == '__main__':
    main()