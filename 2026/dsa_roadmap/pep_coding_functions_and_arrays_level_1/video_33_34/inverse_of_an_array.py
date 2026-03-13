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