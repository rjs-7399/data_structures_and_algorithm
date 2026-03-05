def reverse_an_array(arr):
    begin, end = 0, len(arr) - 1

    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1
    return arr


def main():
    print("Input Array:")
    arr = [
            1, 23, 456, 7, 89,
            1023, -123, 4567, -999,
            7475, 7677, 7879, 8081,
            8283, 8485, 8687, 8889,
            9091, 9293, 4321, 3982
        ]
    print(arr)
    print("\nReversed array")
    ans = reverse_an_array(arr)
    print(ans)

if __name__ == "__main__":
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air video_29_30 % python3 reverse_an_array_2.py
Input Array:
[1, 23, 456, 7, 89, 1023, -123, 4567, -999, 7475, 7677, 7879, 8081, 8283, 8485, 8687, 8889, 9091, 9293, 4321, 3982]

Reversed array
[3982, 4321, 9293, 9091, 8889, 8687, 8485, 8283, 8081, 7879, 7677, 7475, -999, 4567, -123, 1023, 89, 7, 456, 23, 1]
"""
