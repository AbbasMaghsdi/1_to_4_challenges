def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    longest_sequence = []

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            current_sequence = [num]

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                current_sequence.append(current_num)

            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_sequence = current_sequence

    return longest_streak, longest_sequence

# Example usage
input_nums = [100, 4, 200, 1, 3, 2]
longest_streak, longest_sequence = longest_consecutive(input_nums)
print(f"Output: {longest_streak} (sequence: {longest_sequence})")
# Output: 4 (sequence: [1, 2, 3, 4])
