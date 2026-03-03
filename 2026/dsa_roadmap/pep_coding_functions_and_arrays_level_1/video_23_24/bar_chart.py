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
    maxium = find_maximum_from_array(arr)
    bar_chart(arr, maxium)

if __name__ == "__main__":
    main()