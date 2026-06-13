def move_zeros(nums):
  left = 0
  for right in range(len(nums)):
    if nums[right] > 0:
      tmp = nums[left]
      nums[left] = nums[right]
      nums[right] = tmp
      left += 1

nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)