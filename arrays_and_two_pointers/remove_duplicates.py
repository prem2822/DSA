def remove_duplicates(nums):
  left = 0
  for right in range(1,len(nums)):
    if nums[right] != nums[left]:
      left += 1
      nums[left] = nums[right]
  return left + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
print(nums)