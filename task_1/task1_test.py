from task_1.task1 import get_k_elements


def test_regular() -> None:
    """
    Test to determine a regular input to the 'get_k_elements' method

    :return: None
    """
    values = [1, 2, 3, 4, 4, 5, 5]
    k = 3

    result = get_k_elements(values, k)

    assert len(result) == 3


def test_k_equal_n() -> None:
    """
    Test to determine whether method 'get_k_elements' returns all non-repeating values
    when n==k

    :return: none
    """

    values = [1, 2, 3, 4, 5]
    k = 5

    result = get_k_elements(values, k)

    assert len(result) == 5


def test_k_more_than_non_repeating_values() -> None:
    """
    Test to determine whether method 'get_k_elements' behaves well if k is more than
    non-repeating elements in the input list
    :return: None
    """

    values = [1, 2, 3, 4, 4, 5, 5]
    k = 10

    result = get_k_elements(values, k)

    assert len(result) == 5


if __name__ == "__main__":
    test_regular()
    test_k_equal_n()
    test_k_more_than_non_repeating_values()
    print('\nAll tests passed!')
