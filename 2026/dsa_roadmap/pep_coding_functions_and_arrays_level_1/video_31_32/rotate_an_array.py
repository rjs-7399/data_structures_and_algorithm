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
