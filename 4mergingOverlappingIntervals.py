def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Convert each tuple to a list to allow modification
    intervals = [list(interval) for interval in intervals]
    
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        # If merged is empty or the current interval does not overlap with the last merged interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is overlap, so merge the current interval with the last interval in merged
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    # Convert lists back to tuples before returning
    return [tuple(interval) for interval in merged]

# Example usage
input_intervals = [(1, 3), (2, 6), (8, 10)]
merged_intervals = merge_intervals(input_intervals)
print(f"Output: {merged_intervals}")
# Output: [(1, 6), (8, 10)]
