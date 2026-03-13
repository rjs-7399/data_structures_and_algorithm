def inverse_of_an_array(arr):
    buffer = {}
    inverse_arr = [0] * len(arr)

    for i in range(0, len(arr)):
        buffer[arr[i]] = i
        print(f"Printing buffer at index {i}: {buffer}")

    for i in range(0, len(arr)):
        inverse_arr[i] = buffer[i]

    return inverse_arr

def main():
    arr = [3, 4, 1, 2, 0]
    print("Input Array:")
    print(arr)
    print("\nPrinting Buffer Dictionary:")
    ans = inverse_of_an_array(arr)
    print("\nOutput Array after inverse operation:")
    print(ans)

if __name__ == "__main__":
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air video_33_34 % python3 inverse_of_an_array.py 
Input Array:
[3, 4, 1, 2, 0]

Printing Buffer Dictionary:
Printing buffer at index 0: {3: 0}
Printing buffer at index 1: {3: 0, 4: 1}
Printing buffer at index 2: {3: 0, 4: 1, 1: 2}
Printing buffer at index 3: {3: 0, 4: 1, 1: 2, 2: 3}
Printing buffer at index 4: {3: 0, 4: 1, 1: 2, 2: 3, 0: 4}

Output Array after inverse operation:
[4, 2, 3, 0, 1]
"""
