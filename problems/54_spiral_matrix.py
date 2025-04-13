"""
1 2 3
4 5 6
7 8 9

- Here the correct answer will be [1,2,3,6,9,8,7,4,5].
- Here we can add two conditions. We need to move in slice.
- So first we will traverse first row from left to right only.
- Once the boundary hits, we will change the direction and traverse the last column only.
- Once the boundary hits, we will change the direction and traverse the last row from right to left.
- Once the boundary hits, we will change the direction from bottom to top.
- At last we will traverse middle row from left to right.

Test Case 1:
[[1,2,3], [4,5,6], [7,8,9]]

[1,2,3,6,9,8,7,4,5]

[[1,2,3,4], [5,6,7,8], [9,10,11,12]]

[1,2,3,4,8,12,11,10,9,5,6,7]


[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

[1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]

Algorithm:

Initialize empty result list

While elements exists in matrix:

step 1: Pop the first row and append it to the result.

step 2: If matrix exist and 0th element in matrix exist then Append the last element of each subarray to the result.

step 3: If matrix exist then append the last row in reversal order

step 4: If matrix exist and 0th element of matrix exist then append the first element of all rows in the reverse order

[1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]

Dry Run

1, 2, 3, 4, 5
6, 7, 8, 9, 10
11,12,13,14,15
16,17,18,19,20

[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

result = []
While element exist in matrix = True

First iteration

step 1 = Pop the first row and append it to the result array
    - Current matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
    - result = [1,2,3,4,5]

step 2 = matrix exist and first element also exist
    - Current matrix = [[6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
    - result = [1,2,3,4,5] + 10 + 15 + 20 = [1,2,3,4,5,10,15,20]

step 3 = matrix exist then append last row in reverse order
    - Current matrix = [[6,7,8,9], [11,12,13,14], [16,17,18,19]]
    - result = [1,2,3,4,5,10,15,20] + [19,18,17,16] = [1,2,3,4,5,10,15,20,19,18,17,16]

step 4 = If matrix exist and 0th element exist then append the first element of all rows in reversal order.
    - Current matrix = [[6,7,8,9], [11,12,13,14]]
    - result = [1,2,3,4,5,10,15,20] + [11,6] = [1,2,3,4,5,10,15,20,11,6]

Second iteration

step 1 = Pop the first row and append it to the result
    - Current matrix = [[7,8,9], [12,13,14]]
    - result = [1,2,3,4,5,10,15,20,11,6] + 7 + 8 + 9 = [1,2,3,4,5,10,15,20,11,6,7,8,9]

step 2 = matrix exist and first element also exist then append last element of each row
    - Current matrix = [[12,13,14]]
    - result = [1,2,3,4,5,10,15,20,11,6,7,8,9,14]

step 3 = matrix exist then append the last row of matrix in reverse order
    - Current matrix = [[12,13]]
    - result = [1,2,3,4,5,10,15,20,11,6,7,8,9,14,13,12]

step 4 = No more elements left in the matrix
"""

def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

    result_1 = spiralOrder(m1)
    print(result_1)

    result_2 = spiralOrder(m2)
    print(result_2)
