INPUT_FILENAME = 'input.txt'
OUTPUT_FILENAME = 'output.txt'
NUMBER_OF_ELEMENTS = 5


def get_k_elements(values: list, k: int) -> list:
    """
    Picks k elements from the input list and returns them in a new list.

    Complexity analysis:
        cast to set - O(values)
        pop k elements - O(k)

        => Total complexity = O(values) + O(k)

    :param values: list with elements
    :param k: number of elements to pop
    :return: list of k non-repeating elements from input list
    """

    values = set(values)
    if len(values) < k:
        print(f'Not enough non-repeating elements in input list. Returning {len(values)} values')
        return list(values)
    return [values.pop() for _ in range(k)]


if __name__ == "__main__":
    with open(INPUT_FILENAME, 'r') as file:
        values = file.read().split()

    result = get_k_elements(values, NUMBER_OF_ELEMENTS)
    print(" ".join(result))

    with open(OUTPUT_FILENAME, 'w') as file:
        file.write(" ".join(result))
