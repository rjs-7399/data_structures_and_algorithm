def subarray_of_an_array(str):

    sub_arr = []

    for i in range(1, len(str)+1):
        for j in range(0, i):
            sub_arr.append(str[j:i])
            print(f"Sub Arrays at index {i}: {sub_arr}")

    return sub_arr


def main():
    print("Input String:")
    str = "abc"
    print(str)
    print("\nPrinting Sub Arrays:")
    ans = subarray_of_an_array(str)
    print("\nPrinting all possible Sub Arrays:")
    print(ans)


if __name__ == "__main__":
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air video_35_36 % python3 subarray_of_an_array.py
Input String:
abc

Printing Sub Arrays:
Sub Arrays at index 1: ['a']
Sub Arrays at index 2: ['a', 'ab']
Sub Arrays at index 2: ['a', 'ab', 'b']
Sub Arrays at index 3: ['a', 'ab', 'b', 'abc']
Sub Arrays at index 3: ['a', 'ab', 'b', 'abc', 'bc']
Sub Arrays at index 3: ['a', 'ab', 'b', 'abc', 'bc', 'c']

Printing all possible Sub Arrays:
['a', 'ab', 'b', 'abc', 'bc', 'c']
"""
