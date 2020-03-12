# Clover-test-task
A test task implementation for Clover company

## Task 1
Given a list of length N, output K non-overlapping elements.

## Task 2a
Given a list such as
```
time                       value
2016-11-03 11:13:30        23
2016-11-03 11:13:31        13
2016-11-03 11:13:32        15
...
```

Collect statistics for each sliding window of 100 seconds. 
Statistics are:
- median value
- average value
- min value
- max value

Resulting output is:
```
{
  "12.03.2020 09:30:31": {
      "median": 3.5,
      "average": 3.4,
      "min": 99,
      "max": 991
    }
  "12.03.2020 09:30:32": {...}
}
```

## Task 2b
Collect statistics as in 2a, but group them by day.
Resulting output is:
```
{
  "12.03.2020": {
    "12.03.2020 09:30:31": {
      "median": 3.5,
      "average": 3.4,
      "min": 99,
      "max": 991
    }
    "12.03.2020 09:30:32": {...}
  }
  "13.03.2020": {...}
}
```

## Remarks
For each of the tasks, there is a sample input, generated randomly, and corresponding output of the program.
