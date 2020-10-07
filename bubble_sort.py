def bubble_sort(array):
    """
    my own implementation of the bubble sort algorithm.

    Args:
        array (list[int]): A unsorted list with n numbers.

    Returns:
        list[int]: The sorted input list.

    Examples:
        >>> bubble_sort([]) == sorted([])
        True

        >>> bubble_sort([1]) == [1]
        True

        >>> bubble_sort([4,3,2,1]) == sorted([4,3,2,1])
        True

        >>> bubble_sort(['a','d','h','c']) == sorted(['a','d','h','c'])
        True
    """

    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


if __name__ == "__main__":
    import doctest
    from random import randint

    doctest.testmod()
    n = input("Please provide the length of the array: ")
    n = int(n)

    random_array = [randint(0, n) for _ in range(n)]
    print(f"Unsorted Array:\n{random_array}")
    print("------------------------------------")

    sorted_array = bubble_sort(random_array)
    print(f"Sorted Array:\n{sorted_array}")

