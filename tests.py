import unittest

from task_1.task1 import get_k_elements
from task_2.task2a import read_data, calculate_time_window_metrics
from task_2.task2b import calculate_grouped_time_window_metrics


class TestTasks(unittest.TestCase):

    def test_regular__task1(self) -> None:
        """
        Test to determine a regular input to the 'get_k_elements' method

        :return: None
        """
        values = [1, 2, 3, 4, 4, 5, 5]
        k = 3

        result = get_k_elements(values, k)

        self.assertTrue(len(result) == 3)

    def test_k_equal_n__task1(self) -> None:
        """
        Test to determine whether method 'get_k_elements' returns all non-repeating values
        when n==k

        :return: none
        """

        values = [1, 2, 3, 4, 5]
        k = 5

        result = get_k_elements(values, k)

        self.assertTrue(len(result) == 5)

    def test_k_more_than_non_repeating_values__task1(self) -> None:
        """
        Test to determine whether method 'get_k_elements' behaves well if k is more than
        non-repeating elements in the input list
        :return: None
        """

        values = [1, 2, 3, 4, 4, 5, 5]
        k = 10

        result = get_k_elements(values, k)

        self.assertTrue(len(result) == 5)

    def test__regular__task2a(self):
        data = read_data('task_2/input_2a.txt')
        result = calculate_time_window_metrics(data, 100)

        self.assertTrue(result)
        self.assertTrue(result['2020-03-12 20:16:48'] == {"median": 531.0, "average": 527.8, "min": 10, "max": 992})

    def test__empty_window__task2a(self):
        data = read_data('task_2/input_2a.txt')
        try:
            result = calculate_time_window_metrics(data, 0)
            self.fail()
        except ValueError:
            pass

    def test__regular__task2b(self):
        data = read_data('task_2/input_2b.txt')
        result = calculate_grouped_time_window_metrics(data, 100)

        self.assertTrue(result)
        self.assertTrue(
            result['2020-03-12']['2020-03-12 20:23:30'] == {"median": 508.0, "average": 526.0, "min": 18, "max": 999})

    def test__empty_window__task2b(self):
        data = read_data('task_2/input_2b.txt')
        try:
            result = calculate_grouped_time_window_metrics(data, 0)
            self.fail()
        except ValueError:
            pass


if __name__ == "__main__":
    unittest.main()
