import json
from datetime import datetime
from datetime import date
from typing import List, Tuple, Dict

from task_2.task2a import read_data, calculate_sliding_metrics

INPUT_FILENAME = "input_2b.txt"
OUTPUT_FILENAME = 'output_2b.txt'
WINDOW_SIZE = 100


def group_data_by_date(data: List[Tuple[datetime, int]]) -> Dict[date, List[Tuple[datetime, int]]]:
    """
    Groups the data by date, meaning that it groups the input from each day to a separate list,
    creating a dictionary.
    """

    grouped = {}
    cur_day = None

    for date, value in data:
        if date.date() == cur_day:
            grouped[cur_day].append((date, value))
        else:
            cur_day = date.date()
            if grouped.get(cur_day):
                grouped[cur_day].append((date, value))
            else:
                grouped[cur_day] = [(date, value)]

    return grouped


def calculate_grouped_time_window_metrics(
        data: List[Tuple[datetime, int]], window_size: int
) -> Dict[str, Dict[str, float]]:
    """
    The calculate_sliding_metrics is a realization method, which operates on lists without timestamps.
    This method transforms input to pure list, and transforms output to an approachable/serializable format.

    :param data: the timed data in form (datetime, number)
    :param window_size
    :return: serializable dict object with sliding window statistics
    """

    data = group_data_by_date(data)

    result = {}

    for day, day_data in data.items():
        medians, averages, mins, maxs = calculate_sliding_metrics(
            [el[1] for el in day_data], window_size
        )
        result[str(day)] = {}
        for i in range(len(medians)):
            result[str(day)][str(day_data[i][0])] = {
                "median": medians[i],
                "average": averages[i],
                "min": mins[i],
                "max": maxs[i],
            }

    return result


if __name__ == "__main__":
    data = read_data(INPUT_FILENAME)
    result = calculate_grouped_time_window_metrics(data, WINDOW_SIZE)

    json_result = json.dumps(result)  # serializable

    print(json_result)
    with open(OUTPUT_FILENAME, 'w') as file:
        file.write(json_result)
