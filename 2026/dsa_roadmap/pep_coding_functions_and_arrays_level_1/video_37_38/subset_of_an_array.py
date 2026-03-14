def subset_of_an_array(arr):
    length = len(arr)
    result = []
    for i in range(0, pow(2, length)):
        subset = []
        for j in range(0, length):
            if i & pow(2,j) != 0:
                subset.append(arr[j])
        print(f"Printing Subset at index {i}: {subset}")
        result.append(subset)
    return result

def main():
    print("Input Array:")
    arr = [1, 2, 3]
    print(arr)
    print("\nPrinting Subset extraction operations:")
    result = subset_of_an_array(arr)
    print("\nPrinting all possible subsets of the given array:")
    print(result)

if __name__ == "__main__":
    main()

"""CLI Output:
(basevenv) rutvikshah@Rutviks-MacBook-Air video_37_38 % python3 subset_of_an_array.py
Input Array:
[1, 2, 3]

Printing Subset extraction operations:
Printing Subset at index 0: []
Printing Subset at index 1: [1]
Printing Subset at index 2: [2]
Printing Subset at index 3: [1, 2]
Printing Subset at index 4: [3]
Printing Subset at index 5: [1, 3]
Printing Subset at index 6: [2, 3]
Printing Subset at index 7: [1, 2, 3]

Printing all possible subsets of the given array:
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
"""