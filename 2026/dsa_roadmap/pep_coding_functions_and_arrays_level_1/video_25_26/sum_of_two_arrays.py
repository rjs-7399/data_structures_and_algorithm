def sum_of_two_arrays(arr1, arr2):
    carry = 0
    arr3 = []

    if len(arr1) > len(arr2):
        arr2 = [0]*(len(arr1)-len(arr2)) + arr2
    elif len(arr2) > len(arr1):
        arr1 = [0]*(len(arr2)-len(arr1)) + arr1

    for i in range(len(arr1)-1, -1, -1):
        arr3.append((arr1[i] + arr2[i] + carry) % 10)
        print(f"Printing values at each index, current sum: {(arr1[i] + arr2[i] + carry)%10}, Current carry = {(arr1[i] + arr2[i])//10}")
        carry = (arr1[i] + arr2[i] + carry)//10
    if carry != 0:
        arr3.append(carry)

    return arr3[::-1]

def main():
    print("Two input arrays:")
    arr1 = [9, 3, 4, 6, 8]
    arr2 = [1, 9, 8, 8]
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print()
    print("Debugging the Process:")
    result = sum_of_two_arrays(arr1, arr2)
    print("\nSum of two arrays:")
    print(result)

if __name__ == '__main__':
    main()

"""CLI Output
Two input arrays:
Array 1: [9, 3, 4, 6, 8]
Array 2: [1, 9, 8, 8]

Debugging the Process:
Printing values at each index, current sum: 6, Current carry = 1
Printing values at each index, current sum: 5, Current carry = 1
Printing values at each index, current sum: 4, Current carry = 1
Printing values at each index, current sum: 5, Current carry = 0
Printing values at each index, current sum: 9, Current carry = 0

Sum of two arrays:
[9, 5, 4, 5, 6]
"""
