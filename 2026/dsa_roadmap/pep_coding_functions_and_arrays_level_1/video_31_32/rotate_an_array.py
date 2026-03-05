def rotate_an_array(arr, rotation):

    if rotation < 0:
        rotation = len(arr) + rotation
    rotation_index = 1

    while rotation:
        arr = [arr[len(arr)-1]] + arr[:len(arr)-1]
        rotation -= 1
        print(f"Array after rotation: {rotation_index} is {arr}")
        rotation_index += 1

    return arr


def main():
    print("Input array:")
    arr = ["a", "b", "c", "d", "e"]
    print(arr)
    rotation = 6
    print(f"\nNumber of rotations we want to perform: {rotation}")
    ans = rotate_an_array(arr, rotation)

    print(f"\nFinal array after {rotation} rotation")
    print(ans)

if __name__ == "__main__":
    main()

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air video_31_32 % python3 rotate_an_array.py                            
Input array:
['a', 'b', 'c', 'd', 'e']

Number of rotations we want to perform: 6
Array after rotation: 1 is ['e', 'a', 'b', 'c', 'd']
Array after rotation: 2 is ['d', 'e', 'a', 'b', 'c']
Array after rotation: 3 is ['c', 'd', 'e', 'a', 'b']
Array after rotation: 4 is ['b', 'c', 'd', 'e', 'a']
Array after rotation: 5 is ['a', 'b', 'c', 'd', 'e']
Array after rotation: 6 is ['e', 'a', 'b', 'c', 'd']

Final array after 6 rotation
['e', 'a', 'b', 'c', 'd']
"""