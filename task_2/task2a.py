import bisect
import json
from datetime import datetime
from typing import List, Tuple, Dict

INPUT_FILENAME = "input_2a.txt"
OUTPUT_FILENAME = 'output_2a.txt'

WINDOW_SIZE = 100


def read_data(filename: str) -> List[Tuple[datetime, int]]:
    """
    Assuming that data is tab-separated (as given in the task description)
    """

    with open(filename, "r") as file:
        data = []
        for line in file.readlines():
            line = line.strip().split("    ")
            data.append((datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S"), int(line[1])))

        return data


def calculate_sliding_metrics(
    nums: List[float], window_size: int
) -> Tuple[List[float], List[float], List[float], List[float]]:
    """
    Median calculation desciption:
    First, sort initial window. Then, on each iteration, get the median of existing window
    and slide the window(
        find the element to pop,
        pop it,
        insert the next element from the data to the needed place so that window stays sorted
    )

    Average calculation description:
    First, calculate the initial cumulative sum.
    Then, on each iteration:
        calculate the average (cum_sum / window_size),
        subtract the element to pop from cum_sum (reuse from median calculation),
        add the new-added element to cum_sum (reuse from median calculation)

    Min / Max calculation descrtiption:
    Assuming that we have a sorted window (from median calculation),
    min is the first element and max is the last.

    Complexity analysis (worst case):
        initial sort - O(window_size * log(window_size))
        main loop - O(nums - window_size)
        find element to pop - O(log(window_size))
        pop element - O(window_size)
        insert - O(window_size)
        all others are O(1)

        => Total Complexity = O(nums - window_size) * (O(window_size) + O(log(window_size)))


    :param nums: data - list of numbers
    :param window_size
    :return: tuple of lists for each metric
    :raises Exception if window_size is less than 1
    """

    # median calculation. If length of the list is odd - median is the middle element.
    # if length of the list is even - median is avg between two middle elements.
    median_calculate = (
        (lambda vals: vals[int(len(vals) / 2)])
        if window_size % 2 == 1
        else (lambda vals: (vals[len(vals) // 2 - 1] + vals[len(vals) // 2]) / 2)
    )

    if window_size <= 0:
        raise Exception("Window size is zero or less")

    medians = []
    averages = []
    mins = []
    maxs = []

    window = sorted(nums[0:window_size])
    cum_sum = sum(window)

    for i in range(window_size, len(nums)):
        medians.append(median_calculate(window))
        averages.append(cum_sum / window_size)
        mins.append(window[0])
        maxs.append(window[-1])

        index = bisect.bisect_left(window, nums[i - window_size])

        cum_sum -= window[index]
        cum_sum += nums[i]

        window.pop(index)

        bisect.insort_left(window, nums[i])

    medians.append(median_calculate(window))
    averages.append(cum_sum / window_size)
    mins.append(window[0])
    maxs.append(window[-1])

    return medians, averages, mins, maxs


def calculate_time_window_metrics(
    data: List[Tuple[datetime, int]], window_size: int
) -> Dict[str, Dict[str, float]]:
    """
    The calculate_sliding_metrics is a realization method, which operates on lists without timestamps.
    This method transforms input to pure list, and transforms output to an approachable/serializable format.

    :param data: the timed data in form (datetime, number)
    :param window_size
    :return: serializable dict object with sliding window statistics
    """

    medians, averages, mins, maxs = calculate_sliding_metrics(
        [tup[1] for tup in data], window_size
    )
    result = {}

    for i in range(len(medians)):
        result[str(data[i][0])] = {
            "median": medians[i],
            "average": averages[i],
            "min": mins[i],
            "max": maxs[i],
        }

    return result


if __name__ == "__main__":
    data = read_data(INPUT_FILENAME)
    result = calculate_time_window_metrics(data, WINDOW_SIZE)

    json_result = json.dumps(result)  # serializable

    print(json_result)
    with open(OUTPUT_FILENAME, 'w') as file:
        file.write(json_result)
