def get_span_of_array(arr, HIGH, LOW):

    for i in range(0, len(arr)):
        if arr[i] > HIGH:
            HIGH = arr[i]
        print(f"HIGH at index {i}: {HIGH}")

    for i in range(0, len(arr)):
        if arr[i] < LOW:
            LOW = arr[i]
        print(f"LOW at index {i}: {LOW}")

    return HIGH - LOW


def main():
    arr = [6, 15, 30, 40, 4, 11, 9]
    HIGH = -9999
    LOW = 9999
    print("Given Array is:")
    print(arr)
    result = get_span_of_array(arr, HIGH, LOW)
    print("Print the span of given array")
    print(result)

if __name__ == "__main__":
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air video_19_20 % python3 span_of_array.py 
Given Array is:
[6, 15, 30, 40, 4, 11, 9]
HIGH at index 0: 6
HIGH at index 1: 15
HIGH at index 2: 30
HIGH at index 3: 40
HIGH at index 4: 40
HIGH at index 5: 40
HIGH at index 6: 40
LOW at index 0: 6
LOW at index 1: 6
LOW at index 2: 6
LOW at index 3: 6
LOW at index 4: 4
LOW at index 5: 4
LOW at index 6: 4
Print the span of given array
36
"""
