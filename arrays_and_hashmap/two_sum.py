nums = [3, 4, 2]
target = 6
def two_sum(nums, target):
  dict_val = {}
  for i in range(len(nums)):
    balance = target - nums[i]   
    if balance in dict_val:
      return [dict_val[balance], i]
    else:
      dict_val[nums[i]] = i