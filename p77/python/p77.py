
def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    merged_intervals = []
    for interval in sorted_intervals:
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            merged_intervals.append(interval)

    return merged_intervals
