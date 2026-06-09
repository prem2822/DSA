def find_two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]  # 1-based
        elif total < target:
            left += 1
        else:
            right -= 1

    return []  # guaranteed not reached