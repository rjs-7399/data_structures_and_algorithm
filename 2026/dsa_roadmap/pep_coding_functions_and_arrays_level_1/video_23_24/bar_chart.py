def find_maximum_from_array(arr):
    MAX = -9999
    for i in range(0, len(arr)):
        if arr[i] > MAX:
            MAX = arr[i]
    return MAX

def bar_chart(arr, max):
    for floor in range(max, 0, -1):
        for i in range(len(arr)):
                if arr[i] >= floor:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

def main():
    arr = [3, 1, 0, 7, 5]
    print("Given array is")
    print(arr)
    maxium = find_maximum_from_array(arr)
    print("\nMaximum is")
    print(maxium)
    print("\nBelow is the Bar Chart as per given array")
    bar_chart(arr, maxium)

if __name__ == "__main__":
    main()

"""
(basevenv) rutvikshah@Rutviks-MacBook-Air video_23_24 % python3 bar_chart.py
Given array is
[3, 1, 0, 7, 5]

Maximum is
7

Below is the Bar Chart as per given array
   * 
   * 
   **
   **
*  **
*  **
** **
"""
